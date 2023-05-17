
#!--------------------------------------------------------------------------------- INIT_BLOCK---------------------------------------------------------------------------------------------------
DICT_FOR_VALIDATION = {     'mysql': {
                            'host': 'localhost',
                            'database': 'test',
                            'user': 'root',
                            'password': 'пароль'      
                        },

                        'rows': {'total_rows': None, 
                                'percent_of_redzone_strings': None,
                                'percent_of_greenzone_strings': None,
                                'percent_of_bluezone_strings': None},

                        'logger': {
                            'level': ('INFO', 'DEBUG', 'ERROR', 'CRITICAL', 'WARNING'),
                            'log_file_name': 'logging.log'
                        }
                    }
CONFIG_FILE_NAME = "config.ini"
INSERT_QUERY = "INSERT INTO test.new_table4 (ID, ProviderID, Direction, Instrument, CreationDate, ChangeDate, Status, InitialPrice, FillPrice, InitialVolume, FillVolume, Tags, Description, ExtraData) values "
#*--------------------------------------------------------------------------------- GENERATION_PSEUDO_RANDOM_NUMBERS---------------------------------------------------------------------------------------------------
GENERATOR_RANGE_LOW = 0
GENERATOR_RANGE_HIGH = 1
VALUES_FOR_PSEUDORANDOM_GENERATION = {'start_value': {'id':            0.777,
                                                     'provider':       0.666,
                                                     'direction':      0.555,
                                                     'instrument':     0.345,
                                                     'create_date':    0.124,
                                                     'change_date':    0.537,
                                                     'status':         0.899,
                                                     'initial_price':  0.654,
                                                     'fill_price':     0.113,
                                                     'initial_volume': 0.459,
                                                     'fill_volume':    0.523,
                                                     'description':    0.766,
                                                     'extra_data':     0.966,
                                                     'tags':           0.129},

                                      'scale_value': {'id':            666666,
                                                     'provider':       676767,
                                                     'direction':      313131,
                                                     'instrument':     588585,
                                                     'create_date':    343534,
                                                     'change_date':    867549,
                                                     'status':         901233,
                                                     'initial_price':  657485,
                                                     'fill_price':     790372,
                                                     'initial_volume': 754321,
                                                     'fill_volume':    982441,
                                                     'description':    902124,
                                                     'extra_data':     789021,
                                                     'tags':           347777}
                                    }
#*-------------------------------------------------------------------------------------- GENERATION_VALUE_HEX_ID----------------------------------------------------------------------------------------------------------
INCREMENT_FOR_RANDOMNESS = 92832629
NULL_STRING_ORDER = {'id': '104C4DA18', 'provider': None, 
                      'direction': None, 'instrument': None, 
                      'create_date': None, 'create_date': None, 
                      'initial_price': None, 'initial_volume': None, 
                      'tags': None, 'description': None, 
                      'extra_data': None, 'status': None}

#*-------------------------------------------------------------------------------------- GENERATION_VALUE_PROVIDER-------------------------------------------------------------------------------------------------------
PROVIDER_LIST = ["FXCM", "SQM"]

#*-------------------------------------------------------------------------------------- GENERATION_VALUE_DIRECTION------------------------------------------------------------------------------------------------------
DIRECTION_LIST = ["sell", "buy"]

#*-------------------------------------------------------------------------------------- GENERATION_VALUE_INSTRUMENT----------------------------------------------------------------------------------------------------
INSTRUMENT_LIST = ['USDJPY', 'GBPUSD', 'USDCHF', 'AUDUSD',
                   'EURUSD', 'CADPLN', 'NZDJPY', 'GBPCAD',
                   'NZDCHF', 'MXNJPY', 'EURCHF'
                    ]

#*-------------------------------------------------------------------------------------- GENERATION_VALUE_INITIAL_PRICE------------------------------------------------------------------------------------------------
DICT_PRICES =  {'USDJPY': [40.34, 30.95],
                'GBPUSD': [1.30, 1.12],
                'USDCHF': [0.99, 0.9],
                'AUDUSD': [0.720, 0.670],
                'EURUSD': [1.2, 1.03],
                'CADPLN': [3.7, 3.2323],
                'NZDJPY': [88, 80.65],
                'GBPCAD': [1.810, 1.60],
                'NZDCHF': [0.65, 0.55],
                'MXNJPY': [7.11, 6.75],
                'EURCHF': [1.09, 0.946]
                }
#*-------------------------------------------------------------------------------------- GENERATION_VALUE_INITIAL_VOLUME----------------------------------------------------------------------------------------------
VOLUME_LIST = [100000, 10000]

#*-----------------------------------------------------------------------------------------GENERATION_VALUE_СREATE_DATE-----------------------------------------------------------------------------------------------
UNIX_DICT = {'RED_ZONE': [3300, 1, 1, 1669118400],
             'GREEN_ZONE': [78900, 1, 1, 1669122000],
             'BLUE_ZONE': [3300, 1, 1, 1669201200]
             }

FORMAT_FOR_DATATIME = '%Y-%m-%d %H:%M:%S.%f%z'
START_BREAK = 1669158000
END_BREAK = 1669161600
LEAVE_23_CHARACTERS_FIRST = 23
LEAVE_26_CHARACTERS_END = 26
UTC_EXCEL_FORMAT = '+02:00'
UTC_FORMAT = '+0200'
#*-----------------------------------------------------------------------------------------GENERATION_VALUE_СHANGE_DATE-----------------------------------------------------------------------------------------------
ORDER_EXECUTION_TIME = [70, 1]

#*------------------------------------------------------------------------------------------- GENERATION_VALUE_STATUS---------------------------------------------------------------------------------------------------
DICT_STATUS_GENERATE_ALL_ZONES =  {'RED_ZONE'   : {0 : [['done'], 6],  
                                                   1 : [['reject', 'done'], 6],
                                                   2 : [['part fill', 'done'], 6],
                                                   3 : [['fill', 'done'], 6],
                                                   4 : [['in progress', 'reject', 'done'], 6],
                                                   5 : [['in progress', 'part fill', 'done'], 6],
                                                   6 : [['in progress', 'fill', 'done'], 6]},

                                   'GREEN_ZONE' : {0 : [['new', 'in progress', 'reject', 'done'], 2], 
                                                   1 : [['new', 'in progress', 'part fill', 'done'], 2],
                                                   2 : [['new', 'in progress', 'fill', 'done'], 2]},
                                                    
 
                                   'BLUE_ZONE'  : {0 : [['new', 'in progress', 'reject'], 2], 
                                                   1 : [['new', 'in progress', 'part fill'], 2],
                                                   2 : [['new', 'in progress', 'fill'], 2]}
                                                   
                                    }
#*------------------------------------------------------------------------------------GENERATION_VALUE_TAGS_DESCRIPTION_EXTRADATA--------------------------------------------------------------------------------------
DICT_TAGS = {'FXCM' : 'Forex Capital Markets', 'SQM' : 'Sociedad Quimica'}
DICT_DESCRIPTION = {'RED_ZONE': 'Red zone', 'GREEN_ZONE': 'Green zone', 'BLUE_ZONE': 'Blue zone'}
DICT_EXTRA_DATA = {'sell' : 'I sell', 'buy' : 'I buy'}

#*------------------------------------------------------------------------------------------ GENERATION_VALUE_TAGS_FILL_PRICE-------------------------------------------------------------------------------------------
STATUS = ['reject', 'done', 'part fill']

CHECK_PREV_REJECT_STATUS = {True : 0, False : 1}

CHECK_DEPENDMENT_STATUS = {1 : True, 0 : False}

FILL_PRICE_BY_STATUS = {"new"  : False, "in progress" : False,   "reject" : False,
                        "fill" : True,  "part fill" :   True,    "done"   : True
                       }
#*------------------------------------------------------------------------------------------ GENERATION_VALUE_TAGS_FILL_VOLUME---------------------------------------------------------------------------------------
PART_FILL_KOEFICIENTS = {1 : 1, 0 : 0}
FILL_VOLUME_STATUSES_INDEXES = { 'new' : 0,  'in progress' : 0, 'reject' : 0, 'fill' : 1, 'part fill' : 0.1, 'done' : 1}