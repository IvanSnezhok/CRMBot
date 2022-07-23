import csv

from oauth2client.service_account import ServiceAccountCredentials
import gspread
import data.config as cfg
from keyboards.inline.keyboard import check_lists_read


def download_worksheet_as_csv(worksheet_name, file_name):
    try:
        scope = ['https://www.googleapis.com/auth/drive.readonly']
        creds = ServiceAccountCredentials.from_json_keyfile_name('data/google-auth.json', scope)
        client = gspread.authorize(creds)
        spreadsheet = client.open_by_key(cfg.GOOGLE_SHEETS_KEY)

        with open(file_name, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(spreadsheet.worksheet(worksheet_name).get_all_values())

        return True
    except Exception as e:
        print(e)
        return e


def csv_to_dict(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return list(csv.DictReader(lines))


def check_list_1_0():
    worksheet_name = 'Чек-лист1.0'
    file_name = 'check_list_1_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def check_list_2_0():
    worksheet_name = 'Чек-лист2.0'
    file_name = 'check_list_2_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def litniy_maydanchik_1_0():
    worksheet_name = 'Літий майданчик1.0'
    file_name = 'litniy_maydanchik_1_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def litniy_maydanchik_2_0():
    worksheet_name = 'Літий майданчик2.0'
    file_name = 'litniy_maydanchik_2_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def close_check_list_1_0():
    worksheet_name = 'ЗЧек-лист1.0'
    file_name = 'close_check_list_1_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def close_check_list_2_0():
    worksheet_name = 'ЗЧек-лист2.0'
    file_name = 'close_check_list_2_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def close_litniy_maydanchik_1_0():
    worksheet_name = 'ЗЛітий майданчик1.0'
    file_name = 'close_litniy_maydanchik_1_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def close_litniy_maydanchik_2_0():
    worksheet_name = 'ЗЛітий майданчик2.0'
    file_name = 'close_litniy_maydanchik_1_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)

