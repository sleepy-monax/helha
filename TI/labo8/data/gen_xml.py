# %%
import xlrd
from xml.sax.saxutils import escape

# %%


def load_excel(excel_file_path):
    workbook = xlrd.open_workbook(excel_file_path)
    worksheet = workbook.sheet_by_index(0)
    first_row = []  # The row where we stock the name of the column
    for col in range(worksheet.ncols):
        first_row.append(worksheet.cell_value(0, col))
    # transform the workbook to a list of dictionaries
    data = []
    for row in range(1, worksheet.nrows):
        elm = {}
        for col in range(worksheet.ncols):
            elm[first_row[col]] = worksheet.cell_value(row, col)
        data.append(elm)

    return data


accidents = load_excel("TF_ACCIDENTS_2018.xlsx")


# %%
text_keys = {
    'ADM_DSTR_DESCR',
    'BUILD_UP_AREA_DESCR',
    'COLL_TYPE_DESCR',
    'DAY_OF_WEEK_DESCR',
    'LIGHT_COND_DESCR',
    'MUNTY_DESCR',
    'PROV_DESCR',
    'RGN_DESCR',
    'ROAD_TYPE_DESCR',
}

ugly_to_pretty = {
    'DT_DAY': 'day',
    'DT_HOUR': 'hour',
    'CD_BUILD_UP_AREA': 'build-up-area',
    'CD_COLL_TYPE': 'coll-type',
    'CD_DAY_OF_WEEK': 'day-of-week',
    'CD_DSTR_REFNIS': 'dstr-refnis',
    'CD_LIGHT_COND': 'light-cond',
    'CD_MUNTY_REFNIS': 'munty-refnis',
    'CD_PROV_REFNIS': 'prov-refnis',
    'CD_RGN_REFNIS': 'rgn-refnis',
    'CD_ROAD_TYPE': 'road-type',
    'MS_ACCT_WITH_DEAD_30_DAYS': 'acct-with-dead-30-days',
    'MS_ACCT_WITH_DEAD': 'acct-with-dead',
    'MS_ACCT_WITH_MORY_INJ': 'acct-with-mory-inj',
    'MS_ACCT_WITH_SERLY_INJ': 'acct-with-serly-inj',
    'MS_ACCT_WITH_SLY_INJ': 'acct-with-sly-inj',
    'MS_ACCT': 'acct',
    'TX_ADM_DSTR_DESCR_FR': 'adm-dstr-descr-fr',
    'TX_ADM_DSTR_DESCR_NL': 'adm-dstr-descr-nl',
    'TX_BUILD_UP_AREA_DESCR_FR': 'build-up-area-descr-fr',
    'TX_BUILD_UP_AREA_DESCR_NL': 'build-up-area-descr-nl',
    'TX_COLL_TYPE_DESCR_FR': 'coll-type-descr-fr',
    'TX_COLL_TYPE_DESCR_NL': 'coll-type-descr-nl',
    'TX_DAY_OF_WEEK_DESCR_FR': 'day-of-week-descr-fr',
    'TX_DAY_OF_WEEK_DESCR_NL': 'day-of-week-descr-nl',
    'TX_LIGHT_COND_DESCR_FR': 'light-cond-descr-fr',
    'TX_LIGHT_COND_DESCR_NL': 'light-cond-descr-nl',
    'TX_MUNTY_DESCR_FR': 'munty-descr-fr',
    'TX_MUNTY_DESCR_NL': 'munty-descr-nl',
    'TX_PROV_DESCR_FR': 'prov-descr-fr',
    'TX_PROV_DESCR_NL': 'prov-descr-nl',
    'TX_RGN_DESCR_FR': 'rgn-descr-fr',
    'TX_RGN_DESCR_NL': 'rgn-descr-nl',
    'TX_ROAD_TYPE_DESCR_FR': 'road-type-descr-fr',
    'TX_ROAD_TYPE_DESCR_NL': 'road-type-descr-nl',
}


def emit_xml(tag, content):
    return "<%s>%s</%s>" % (tag, content, tag)


def emit_xml_list(tags, content):
    return emit_xml("accidents", "".join(content))


def emit_accident(accident):
    result = ''
    for key in accident:
        result = result + \
            emit_xml(ugly_to_pretty[key], escape(str(accident[key])))

    return result


def emit_accidents(accidents):
    return emit_xml_list("accidents", [emit_xml("accident", emit_accident(acc)) for acc in accidents])


print("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
print("<?xml-stylesheet type=\"text/xsl\" href=\"data.xsl\"?>")
print(emit_accidents(accidents))
