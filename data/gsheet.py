import csv

from oauth2client.service_account import ServiceAccountCredentials
import gspread
import data.config as cfg
from keyboards.inline.keyboard import check_lists_read
from loader import db


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
    result = csv.DictReader(lines, 'Text')
    return list(result)


def check_list_1_0():
    worksheet_name = 'Чек-лист1.0'
    file_name = 'check_list_1_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def check_list_2_0():
    worksheet_name = 'Чек-лист2.0'
    file_name = 'check_list_2_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def litniy_maydanchik_1_0():
    worksheet_name = 'Літній майданчик1.0'
    file_name = 'litniy_maydanchik_1_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def litniy_maydanchik_2_0():
    worksheet_name = 'Літній майданчик2.0'
    file_name = 'litniy_maydanchik_2_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def close_check_list_1_0():
    worksheet_name = 'ЗЧек-лиcт1.0'
    file_name = 'close_check_list_1_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def close_check_list_2_0():
    worksheet_name = 'ЗЧек-лист2.0'
    file_name = 'close_check_list_2_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def close_litniy_maydanchik_1_0():
    worksheet_name = 'ЗЛітній майданчик1.0'
    file_name = 'close_litniy_maydanchik_1_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def close_litniy_maydanchik_2_0():
    worksheet_name = 'ЗЛітній майданчик2.0'
    file_name = 'close_litniy_maydanchik_2_0.csv'
    return download_worksheet_as_csv(worksheet_name, file_name)


def update_all(key=None):
    if key == 'hashtag_1_0':
        check_list_1_0()
        cl1 = csv_to_dict('check_list_1_0.csv')
        temp_cl1_list = []
        for i in range(len(cl1)):
            temp_cl1_list.append(cl1[i])
    elif key == "hashtag_2_0":
        check_list_2_0()
        cl2 = csv_to_dict('check_list_2_0.csv')
        temp_cl2_list = []
        for i in range(len(cl2)):
            temp_cl2_list.append(cl2[i])
    elif key == 'litniy_maydanchik_1_0':
        litniy_maydanchik_1_0()
        lm1 = csv_to_dict('litniy_maydanchik_1_0.csv')
        temp_lm1_list = []
        for i in range(len(lm1)):
            temp_lm1_list.append(lm1[i])
    elif key == 'litniy_maydanchik_2_0':
        litniy_maydanchik_2_0()
        lm2 = csv_to_dict('litniy_maydanchik_2_0.csv')
        temp_lm2_list = []
        for i in range(len(lm2)):
            temp_lm2_list.append(lm2[i])
    elif key == 'close_lists_1_0':
        close_check_list_1_0()
        cl1 = csv_to_dict('close_check_list_1_0.csv')
        temp_cl1_list = []
        for i in range(len(cl1)):
            temp_cl1_list.append(cl1[i])
    elif key == 'close_lists_2_0':
        close_check_list_2_0()
        cl2_close = csv_to_dict('close_check_list_2_0.csv')
        temp_cl2_close_list = []
        for i in range(len(cl2_close)):
            temp_cl2_close_list.append(cl2_close[i])
    elif key == 'close_maydanchik_1_0':
        close_litniy_maydanchik_1_0()
        lm1 = csv_to_dict('close_litniy_maydanchik_1_0.csv')
        temp_lm1_list = []
        for i in range(len(lm1)):
            temp_lm1_list.append(lm1[i])
    elif key == 'close_maydanchik_2_0':
        close_litniy_maydanchik_2_0()
        lm2_close = csv_to_dict('close_litniy_maydanchik_2_0.csv')
        temp_lm2_close_list = []
        for i in range(len(lm2_close)):
            temp_lm2_close_list.append(lm2_close[i])
    elif key is None:
        update_all('hashtag_1_0')
        update_all('hashtag_2_0')
        update_all('litniy_maydanchik_1_0')
        update_all('litniy_maydanchik_2_0')
        update_all('close_lists_1_0')
        update_all('close_lists_2_0')
        update_all('close_maydanchik_1_0')
        update_all('close_maydanchik_2_0')
