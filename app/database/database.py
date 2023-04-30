from datetime import datetime

types = ['level_started', 'level_solved']
details = ['level_1212_001', 'level_1333_034']


events = [
    {'id': 1, 'type': types[(0)], 'detail': 'level_1212_001',
        'timestamp': datetime.now().strftime('%Y-%m-%d, %H:%M:%S'), 'player_id': 1},

    {'id': 2, 'type': types[(1)], 'detail': 'level_1333_034',
     'timestamp': datetime.now().strftime('%Y-%m-%d, %H:%M:%S'), 'player_id': 2}
]


players = [
    {'id': 1, 'name': 'Reijo', 'events': [events[0]]},
    {'id': 2, 'name': 'Veijo', 'events': [events[1]]}
]
