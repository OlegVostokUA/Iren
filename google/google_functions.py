import datetime
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account


CREDENTIALS_FILE = 'vostok-419418-56fa2e5e41fe.json'  # Имя файла с закрытым ключом, вы должны подставить свое
SCOPES_CAL = ["https://www.googleapis.com/auth/calendar"]

def get_auth(id_file):
    '''
    Функция настройки аунтефикации
    '''
    # id_file = id_file
    ### google sheet
    # Читаем ключи из файла
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)  # Выбираем работу с таблицами и 4 версию API
    spreadsheetId = id_file
    ### google calendar
    credentials_calendar = service_account.Credentials.from_service_account_file(
        filename=CREDENTIALS_FILE, scopes=SCOPES_CAL
    )
    service_calendar = apiclient.discovery.build('calendar', 'v3', credentials=credentials_calendar)
    ### google drive
    driveService = apiclient.discovery.build('drive', 'v3', http=httpAuth)  # Выбираем работу с Google Drive и 3 версию API
    access = driveService.permissions().create(
        fileId=spreadsheetId,
        body={'type': 'user', 'role': 'writer', 'emailAddress': 'vostokukrdon@gmail.com'},
        # Открываем доступ на редактирование
        fields='id'
    ).execute()
    return service, spreadsheetId, service_calendar

def read_calendar():
    id_file = '1Uqp9zSn6QffhtKUEM5kEQ1BC7Vgj1OCZRYfEryhduYI' # id pidsobne file
    service, spreadsheetId, service_calendar = get_auth(id_file)

    calendar_list_entry = {
        'id': 'vostokukrdon@gmail.com'
    }
    now = datetime.datetime.now()
    day_of_week = datetime.datetime.weekday(now)
    if day_of_week == 5:
        tomorrow_date = now + datetime.timedelta(days=2)
    else:
        tomorrow_date = now + datetime.timedelta(days=1)

    tomorrow_date = tomorrow_date.strftime('%Y-%m-%d')

    date1 = tomorrow_date+'T04:00:00Z'
    date2 = tomorrow_date + 'T14:00:00Z'

    created_calendar_list_entry = service_calendar.calendarList().insert(body=calendar_list_entry).execute()

    calendar_string = '94 ПРИКЗ:\n'
    page_token = None
    while True:
        events = service_calendar.events().list(
            calendarId='vostokukrdon@gmail.com',
            timeMin=date1,
            timeMax=date2,
            pageToken=page_token).execute()
        for num, event in enumerate(events['items']):
            calendar_string = calendar_string + str(num+1)+'. '+event['summary']+'\n'
        page_token = events.get('nextPageToken')
        if not page_token:
            break

    return calendar_string


def read_pidsobne():
    '''
    Функция чтения файла по ПГ
    '''
    id_file = '1Uqp9zSn6QffhtKUEM5kEQ1BC7Vgj1OCZRYfEryhduYI'  # id pidsobne file
    service, spreadsheetId, service_calendar = get_auth(id_file)
    ranges = ["Лист1!A1:F8"]  #

    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    sheet_values = results['valueRanges'][0]['values']
    string_for_message = 'ПГ:\n'
    for i in sheet_values:
        string_for_message=string_for_message+i[0]+': '+i[1]+' кг / '+i[2]+' кг / '+i[3]+'%\n'

    return string_for_message

def read_central():
    '''
    Функция чтения файла по централизовки
    '''
    id_file = '1QEAGgJmmMa53yTl2UM1-4r3a9Di5sJrUX_S7Qfq3mdM'  # id central file
    service, spreadsheetId, service_calendar = get_auth(id_file)
    ranges = ["Лист1!A1:E15"]  #

    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    sheet_values = results['valueRanges'][0]['values']

    # ['06.1.2/15817-24', '11.03.2024', 'ГЦКБРтаЗ', 'Дієтична добавка Гексавіт', '50000', 'прийом']
    # ['06.1.2/13354-24', '29.02.2024', 'ГЦКБРтаЗ', 'Свинина заморожена', '1550', 'прийом']
    # ['06.1.2/21672-24', '04.04.2024', '2144', 'Дієтична добавка Гексавіт', '25000', 'прийом']
    # ['06.1.2/19617-24', '27.03.2024', 'ГЦКБРтаЗ', 'Блоки заморожені Свинина', '1400', 'прийом']
    # ['06.1.2/19617-24', '27.03.2024', 'ГЦКБРтаЗ', 'Мясо птиці', '1000', 'прийом']
    # ['06.1.2/19499-24', '26.03.2024', '2144', 'Молоко згущене з цукром', '150', 'прийом']
    # ['06.1.2/21671-24', '04.04.2024', 'ГЦКБРтаЗ', 'Сало шпик', '700', 'прийом']

    return sheet_values


def func_parse_central():
    result = read_central()
    return result

# func_parse_central()

def func_parce_foul():
    calendar_string = read_calendar()
    pids_string = read_pidsobne()
    result_fool = calendar_string+pids_string
    return result_fool


def func_parce_short():
    calendar_string = read_calendar()
    result_min = calendar_string[10:]
    return result_min
