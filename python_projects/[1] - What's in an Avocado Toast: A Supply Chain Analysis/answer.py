import pandas as pd

avocado = pd.read_csv('data/avocado.csv', sep='\t')

relevant_columns = [ 'code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins','origins_tags']
avocado = avocado[relevant_columns]

with open("data/relevant_avocado_categories.txt", 'r') as file:
    relevant_avocado_categories = file.read().splitlines()
    file.close()

avocado['categories_list'] = avocado['categories_tags'].str.split(',')
avocado = avocado.dropna(subset = 'categories_list')

avocado = avocado[avocado['categories_list'].apply(lambda x: any([i for i in x if i in relevant_avocado_categories]))]
avocado_united_kingdom = avocado[(avocado['countries'] == 'United Kingdom')]

avocado_origin = (avocado_united_kingdom['origins_tags'].value_counts().index[0])
avocado_origin = avocado_origin.lstrip("en:")

#read_and_filter_data function
def read_and_filter_data(filename, relevant_categories):
    df = pd.read_csv('data/' + filename, sep='\t')

    relevant_columns = [ 'code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins','origins_tags']
    df = df[relevant_columns]

    df['categories_list'] = df['categories_tags'].str.split(',')
    df = df.dropna(subset = 'categories_list')
    df = df[df['categories_list'].apply(lambda x: any([i for i in x if i in relevant_categories]))]

    df_uk = df[(df['countries'] == 'United Kingdom')]

    top_origin_strip = (df_uk['origins_tags'].value_counts().index[0])
    top_origin_country = top_origin_strip.lstrip("en:")
    top_origin_country = top_origin_country.replace('-', ' ')

    print(f'**{filename[:-4]} origins**','\n', top_origin_country, '\n')

    print ("Top origin country: ", top_origin_country)
    print ("\n")

    return top_origin_country

top_avocado_origin = read_and_filter_data('avocado.csv', relevant_avocado_categories)

with open("data/relevant_olive_oil_categories.txt", 'r') as file:
    relevant_olive_oil_categories = file.read().splitlines()
    file.close()

top_olive_oil_origin = read_and_filter_data('olive_oil.csv', relevant_olive_oil_categories)

with open("data/relevant_sourdough_categories.txt", 'r') as file:
    relevant_sourdough_categories = file.read().splitlines()
    file.close()

top_sourdough_origin = read_and_filter_data('sourdough.csv', relevant_sourdough_categories)