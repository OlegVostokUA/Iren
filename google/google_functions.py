import datetime
import httplib2
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2 import service_account


CREDENTIALS_FILE = 'vostok-419418-56fa2e5e41fe.json'  # Имя файла с закрытым ключом, вы должны подставить свое
SCOPES_CAL = ["https://www.googleapis.com/auth/calendar"]

def get_auth():
    '''
    Функция настройки аунтефикации
    '''
    ### google sheet
    # Читаем ключи из файла
    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())  # Авторизуемся в системе
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)  # Выбираем работу с таблицами и 4 версию API
    spreadsheetId = '1Uqp9zSn6QffhtKUEM5kEQ1BC7Vgj1OCZRYfEryhduYI'
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
    service, spreadsheetId, service_calendar = get_auth()

    calendar_list_entry = {
        'id': 'vostokukrdon@gmail.com'
    }

    tomorrow_date = datetime.datetime.now() + datetime.timedelta(days=1)
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
    # page_token = None
    # while True:
    #     calendar_list = service_calendar.calendarList().list(pageToken=page_token).execute()
    #     for calendar_list_entry in calendar_list['items']:
    #         print(calendar_list_entry)
    #     page_token = calendar_list.get('nextPageToken')
    #     if not page_token:
    #         break

    #calendar = service_calendar.calendars().get(calendarId='dm9zdG9rdWtyZG9uQGdtYWlsLmNvbQ').execute()

    #print(calendar['summary'])
    return calendar_string


def read_pidsobne():
    '''
    Функция чтения файла по ПГ
    '''
    service, spreadsheetId, service_calendar = get_auth()
    ranges = ["Лист1!A1:D8"]  #

    results = service.spreadsheets().values().batchGet(spreadsheetId=spreadsheetId,
                                                       ranges=ranges,
                                                       valueRenderOption='FORMATTED_VALUE',
                                                       dateTimeRenderOption='FORMATTED_STRING').execute()
    sheet_values = results['valueRanges'][0]['values']
    string_for_message = 'ПГ:\n'
    for i in sheet_values:
        string_for_message=string_for_message+i[0]+': '+i[1]+' кг / '+i[2]+' кг / '+i[3]+'%\n'

    return string_for_message

def main_func_parce():
    calendar_string = read_calendar()
    pids_string = read_pidsobne()
    result_fool = calendar_string+pids_string
    result_min = calendar_string[10:]
    return result_min, result_fool

res_min, res_fool = main_func_parce()
print(res_min, res_fool)
