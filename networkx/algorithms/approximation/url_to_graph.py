import gspread
import numpy as np
from FastWClq_Algorithm import graph_builder,get_weight_clique


def extract_val(sheet):
    count = 0
    node_l = []
    weight_l = []
    neighbors_l = []
    for i in sheet:
        for j in i:
            if not (j.__eq__("Nodes") or j.__eq__("Weight") or j.__eq__("Neighbors")):
                if count == 0:
                    node_l.append(int(j))
                if count == 1:
                    weight_l.append(int(j))
                if count == 2:
                    neighbors_l.append(j)
        count += 1
    weight_dict = {}
    neighbors_dict = {}
    count = 0
    for i in node_l:
        weight_dict[i]=weight_l[count]
        neighbors_dict[i]=[str.split(neighbors_l[count],",")]
        count += 1
    return weight_dict,neighbors_dict





def clique_to_sheet(input,url):
    out = 'Output'
    account = gspread.service_account(url)
    spreadsheet = account.open("Create Your Graph")
    input_graph = spreadsheet.worksheet(input)
    try:
        output_graph = spreadsheet.worksheet(out)
        spreadsheet.del_worksheet(output_graph)
    except:
        print("No output")
    g_val = input_graph.get_all_values()
    weight_dict, neighbors_dict= extract_val(g_val)
    g = graph_builder(weight_dict, neighbors_dict)
    title = "Output"
    spreadsheet.add_worksheet(title=title,rows=4, cols=len(g[0])+1)
    clique_sheet = spreadsheet.worksheet(title)
    clique_sheet.update('A1', 'Nodes')
    clique_sheet.update('A2', 'Clique Weight')
    char = chr(ord('B'))
    for i in g[0]:
        clique_sheet.update(char+str(1),i)
        char = chr(ord(char)+1)
    clique_sheet.update('B2',g[1])



    #last_cell = chr(ord('A') + (result.shape[1] - 1)) + str(result.shape[0])
    # sheet_to_write = "A1:" + last_cell
    # result_matrix.update(sheet_to_write, result.tolist())


# if __name__ == '__main__':
#     clique_to_sheet("Input")
