import contextlib
import io
import runpy
import unittest
from datetime import date
from decimal import Decimal
from unittest.mock import MagicMock, patch

import main_code


class InventoryChecks(unittest.TestCase):
    def run_output(self, function, database):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            function(database)
        return output.getvalue()

    def test_view_distinguishes_sold_and_unsold(self):
        database = MagicMock()
        database.cursor.return_value.fetchall.return_value = [
            (1, date(2026, 1, 5), Decimal("25.00"), Decimal("40.00")),
            (2, date(2026, 1, 12), Decimal("18.50"), None),
        ]
        output = self.run_output(main_code.view_items, database)
        self.assertIn("Sale Price: $40.00", output)
        self.assertIn("Sale Price: Not sold", output)

    def test_empty_inventory(self):
        database = MagicMock()
        database.cursor.return_value.fetchall.return_value = []
        self.assertIn("No items were found", self.run_output(main_code.view_items, database))

    def test_add_unsold_item_commits_parameters(self):
        database = MagicMock()
        with patch("builtins.input", side_effect=["2026-01-05", "25", ""]):
            self.run_output(main_code.add_item, database)
        query, parameters = database.cursor.return_value.execute.call_args.args
        self.assertEqual(parameters, (date(2026, 1, 5), 25.0, None))
        self.assertIn("%s", query)
        database.commit.assert_called_once()

    def test_negative_prices_rejected_before_insert(self):
        for prices in [("-1", ""), ("25", "-1")]:
            with self.subTest(prices=prices):
                database = MagicMock()
                with patch("builtins.input", side_effect=["2026-01-05", *prices]):
                    with self.assertRaises(ValueError):
                        main_code.add_item(database)
                database.cursor.assert_not_called()

    def test_invalid_date_rejected(self):
        database = MagicMock()
        with patch("builtins.input", return_value="2026-02-30"):
            with self.assertRaises(ValueError):
                main_code.add_item(database)
        database.cursor.assert_not_called()

    def test_profit_display_uses_aggregate(self):
        database = MagicMock()
        database.cursor.return_value.fetchone.return_value = (Decimal("12.50"),)
        self.assertIn("Total profit: $12.50", self.run_output(main_code.calculate_profit, database))

    def test_empty_profit_displays_zero(self):
        database = MagicMock()
        database.cursor.return_value.fetchone.return_value = (None,)
        self.assertIn("Total profit: $0.00", self.run_output(main_code.calculate_profit, database))

    def test_menu_handles_invalid_choice_and_closes(self):
        database = MagicMock()
        with patch.object(main_code.mysql.connector, "connect", return_value=database):
            with patch("builtins.input", side_effect=["wrong", "q"]):
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    main_code.main()
        self.assertIn("Invalid option", output.getvalue())
        self.assertIn("Program closed", output.getvalue())
        database.close.assert_called_once()

    def test_connection_error_is_reported(self):
        with patch.object(main_code.mysql.connector, "connect", side_effect=main_code.Error("test failure")):
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                main_code.main()
        self.assertIn("Could not connect to the database", output.getvalue())

    def test_environment_and_certificate_settings(self):
        settings = {"DB_HOST": "example.invalid", "DB_USER": "test_user",
                    "DB_PASSWORD": "dummy-test-value", "DB_NAME": "test_database",
                    "DB_PORT": "3307", "DB_SSL_CA": "test-ca.pem"}
        with patch.dict("os.environ", settings, clear=True):
            config = runpy.run_path("db_config.py")["DB_CONFIG"]
        self.assertEqual(config["host"], "example.invalid")
        self.assertEqual(config["password"], "dummy-test-value")
        self.assertEqual(config["port"], 3307)
        self.assertTrue(config["ssl_verify_cert"])
        self.assertTrue(config["ssl_verify_identity"])
        self.assertFalse(config["ssl_disabled"])


if __name__ == "__main__":
    unittest.main()
