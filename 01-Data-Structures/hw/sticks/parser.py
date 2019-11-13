from operator import itemgetter


def parse_to_int(data_to_parse):
    for i in range(len(data_to_parse)):
        if data_to_parse[i]['price'] != 'null':
            data_to_parse[i]['price'] = int(data_to_parse[i]['price'])
        else:
            data_to_parse[i]['price'] = 0
        if data_to_parse[i]['points'] != 'null':
            data_to_parse[i]['points'] = int(data_to_parse[i]['points'])
        else:
            data_to_parse[i]['points'] = 0


def json_parser(file_name):
    parsed_file = []
    with open(file_name, "r") as read_file:
        data = read_file.read()
        data = data[1:-1]
        text = data.split('}, ')
        text = [s[1:] for s in text if s[0][0] == '{']
        text[-1] = text[-1][:-1]
        for i in range(len(text)):
            text[i] = text[i].replace('": ', '^')
            text[i] = text[i].split(', "')
            text[i] = [s.replace('"', '') for s in text[i]]
            parsed_file.append(dict([i.split('^') for i in text[i]]))
    parse_to_int(parsed_file)
    return parsed_file


def merge_files(file_1, file_2):
    file = []
    file.extend(file_1)
    file.extend(file_2)
    unique_sets = set(frozenset(d.items()) for d in file)
    file = [dict(s) for s in unique_sets]
    return file


# В задании 3 "Madera" не является сортом вина, а регионом,
# поэтому статистика для неё не высчитывалась
def sorts_statistics(data):
    sorts = {'Gew\\u00fcrztraminer', 'Riesling',
             'Merlot', 'Tempranillo', 'Red Blend'}
    statistics = {}
    for i in sorts:
        temp = [s for s in data if s['variety'] == i]
        prices = [p['price'] for p in data if p['price'] != 0 and p['variety'].find(i) != -1]
        countries = [p['country'] for p in temp]
        regions = [p['region_1']for p in temp if p['region_1'] != 'null']
        points = [p['points'] for p in temp if p['points'] != 0]
        country_pair = max(zip((countries.count(item) for item in set(countries)),
                               set(countries)))
        region_pair = max(zip((regions.count(item) for item in set(regions) if item != 'null'),
                              set(regions)))
        average_score = sum(points) // len(points)
        min_price = min(prices)
        max_price = max(prices)
        average_price = sum(prices) / len(prices)
        item = dict({'average_price': average_price})
        item.update({'min_price': min_price})
        item.update({'max_price': max_price})
        item.update({'most_common_country': country_pair[1]})
        item.update({'most_common_region': region_pair[1]})
        item.update({'average_score:': average_score})
        statistics.update({i: item})
    return statistics


def avrg_producing(data):
    avrg = {}
    keys = [[key for key, values in i.items()] for i in data]
    keys = [val for sublist in keys for val in sublist]
    keys_pair = dict(zip(set(keys), (keys.count(item) for item in set(keys))))
    keys = set(keys)
    avrg = {key: 0 for key in keys}
    for i in data:
        for key, value in i.items():
            avrg[key] += value
    avrg = [(key, avrg[key] // keys_pair[key]) for key in keys]
    max_v = max(i[1] for i in avrg)
    max_v = {i[0]: i[1] for i in avrg if max_v == i[1]}
    min_v = min(i[1] for i in avrg)
    min_v = {i[0]: i[1] for i in avrg if min_v == i[1]}
    return max_v, min_v


def general_statistics(data):
    statistics = {}
    expensive_wines = [i['title'] for i in data if data[0]['price'] == i['price']]
    c_wines = [i for i in data if i['price'] != 0]
    c_wines = [i['title'] for i in c_wines if c_wines[-1]['price'] == i['price']]
    highest_score = max([i['points'] for i in data])
    lowest_score = min([i['points'] for i in data])
    countries_p = [{p['country']: p['price']} for p in data if p['price'] != 0]
    countries_r = [{p['country']: p['points']} for p in data if p['points'] != 0]
    most_exp_c, cheapest_c = avrg_producing(countries_p)
    most_rated_c, underrated_c = avrg_producing(countries_r)
    testers = [p['taster_name'] for p in data if p['taster_name'] != 'null']
    testers = max(zip((testers.count(item) for item in set(testers)),
                      set(testers)))
    testers = testers[1]
    statistics.update({'most_expensive_wines': str(expensive_wines)})
    statistics.update({'cheapest_wines': c_wines})
    statistics.update({'highest_score': highest_score})
    statistics.update({'lowest_score': lowest_score})
    statistics.update({'most_expensive_country': most_exp_c})
    statistics.update({'cheapest_country': cheapest_c})
    statistics.update({'most_rated_country': most_rated_c})
    statistics.update({'underrated_country': underrated_c})
    statistics.update({'most_active_commentator': testers})
    return statistics


def dumper_json(data, filename):
    with open(filename, "w") as file_handler:
        dumped_f = str(data)
        dumped_f = dumped_f.replace('"null"', 'null').replace(" '", ' "')
        dumped_f = dumped_f.replace("':", '":').replace("',", '",')
        dumped_f = dumped_f.replace("{'", '{"').replace("'}", '"}')
        dumped_f = dumped_f.replace("\"['", '["').replace("']\"", '"]')
        dumped_f = dumped_f.replace("['", '["').replace("']", '"]')
        file_handler.write(dumped_f)
        return dumped_f


def int_to_string(data):
    for i in range(len(data)):
        if winedata[i]['price'] == 0:
            winedata[i]['price'] = 'null'
        if winedata[i]['points'] == 0:
            winedata[i]['points'] = 'null'
        data[i]['points'] = str(data[i]['points'])
    return data

def markdown_dumper(data):
    markdown = data
    markdown = markdown.replace('[', '\n').replace('{', '\n').replace('}', '\n').replace(']', '\n')
    markdown = markdown.replace('"', "`").replace(',', '\n').replace(':', ':\t')
    return markdown

winedata_1 = json_parser("./winedata_1.json")
winedata_2 = json_parser("./winedata_2.json")
winedata = merge_files(winedata_1, winedata_2)
winedata = sorted(winedata, key=itemgetter('variety'))
winedata = sorted(winedata, key=itemgetter('price'), reverse=True)
stats = sorts_statistics(winedata)
gen_stats = general_statistics(winedata)
winedata = int_to_string(winedata)
stats = dict(wine=stats)
stats = list([stats, gen_stats])
filename = "./stats.json"
test = dumper_json(stats, filename)
dumper_json(winedata, "./winedata_full.json")
md = markdown_dumper(test)
with open('stats.md', 'w') as file_handler:
    file_handler.write(md)
