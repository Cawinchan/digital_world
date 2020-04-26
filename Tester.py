# reading the data
with open('/home/cappy/Downloads/c_incunabula.txt') as f:
    strng = f.read()
    f.close()

strng = strng.split('\n')
s1 = strng[0].split(' ')

no_of_books = int(s1[0])
no_of_lib = int(s1[1])
no_of_days = int(s1[2])

book_scores = strng[1]
book_scores = book_scores.split(' ')

lib_data_temp = []

for i in range(2, len(strng)):
    lib_data_temp.append(strng[i].split(' '))

lib_data = []

for i in range(0, len(lib_data_temp) - 1, 2):
    if (i + 1) > len(lib_data_temp):
        break
    lst = []

    for j in lib_data_temp[i]:
        lst.append(j)

    lib_data.append([lst, lib_data_temp[i + 1]])


# print (book_scores)


[[6,2,2],[1.2.3],]

# processing the data
# print (type(lib_data[0][1]))

[['0',4],['1',1],['2',3]]

def library_scoring_system(lib_data, book_score_lst, total_given_days):
    ''' takes in lib_data and scores it by cawin's method
        input: lst of lst of lib_data

        output: score_dict key - lib_id (str)
                           value - score (int)'''
    score_lst = []
    scanned_books = []

    for library in range(no_of_lib):
        lib_id = str(library)
        sign_up_length = int(lib_data[library][0][1])
        shipment_rate = int(lib_data[library][0][2])
        str_to_int = list(map(int, lib_data[library][1]))
        total_score_possible = 0
        for j in str_to_int:
            for i in range(len(book_score_lst)):
                if book_score_lst[i][0] == j:
                    total_score_possible += book_score_lst[i][1]
                    # print(total_score_possible)
                    break
        scanned_books.append(lib_data[library][1])
        score_of_library = (total_score_possible / shipment_rate) - (sign_up_length * shipment_rate)
        score_lst.append([lib_id, score_of_library])
        score_lst.sort(key=sortSecond, reverse=True)
    return score_lst
    # returns lib_id and score


# input is a list of books ordering their values
def sortSecond(val):
    return val[1]


def format_lib(book_scores):
    book_score_lst = []
    for i in range(len(book_scores)):
        book_score_lst.append([i, int(book_scores[i])])

    book_score_lst.sort(key=sortSecond, reverse=True)

    return book_score_lst


def total_libraries_used(lst, lib_data, total_given_days):
    ''' input: lst of scoring and lib and lib_data
        output: total number of possible libraries to sign up
        '''
    counter = 0
    for library in range(len(lst)):
        sign_up_days = int(lib_data[library][0][1])
        # print('test', sign_up_days)
        if total_given_days - sign_up_days > 0:
            total_given_days -= sign_up_days
            # print(total_given_days)
            counter += 1
    return counter


book_score_lst = format_lib(book_scores)
lib_ids = library_scoring_system(lib_data, book_score_lst, no_of_days)
total_libs_used = total_libraries_used(lib_ids, lib_data, no_of_days)

# print(lib_ids)
# print(total_libraries_used)
# returns lib id[0][0] and lib id[1][0]
# send everything

returnlst = []
# for i in range(len(lib_ids)):
#     libid = int(lib_ids[i][0])
#     lst = []
#     lst.append([libid, lib_data[i][0][0]])
#     #lst.append(lib_data[i][0][0])
#     templst = []
#     for x in range(int(lib_data[i][0][0])):
#         templst.append(book_score_lst[x][1])
#     lst.append(templst)

#     returnlst.append(lst)

for i in lib_ids:
    libid = i[0]
    lst = []
    lst.append([libid, lib_data[int(libid)][0][0]])
    # lst.append(lib_data[i][0][0])
    templst = []
    for x in range(int(lib_data[int(libid)][0][0])):
        if not (str(book_score_lst[x][1]) not in lib_data[int(libid)][1]):
            templst.append(book_score_lst[x][1])
    lst.append(templst)
    # print (lst)
    count = len(lst[1])
    lst[0][1] = str(count)

    returnlst.append(lst)

# print (returnlst)

library = returnlst

# outputting the data
'''
What I need
lib_scan = total number of libraries being scanned
lib_out = required data in the format (first signup appears first)
[[[library_id, num_of_books_for_scanning][books_sent_in_order]], --- (for all the libraries)]
'''

with open('out.file', 'w') as f:
    f.write(str(total_libs_used))
    f.write('\n')

    for library in returnlst:
        f.write(str(library[0][0]) + ' ' + str(library[0][1]))
        f.write('\n')
        for info in library[1]:
            f.write(str(info) + ' ')
        f.write('\n')

    f.close()


