# print_list_index_for_given_ind
def main():
    pass
    n=input()
    list_1=list(n)
    list_2=[]
    sli=0
    for word in list_1:
        if word.isalnum():
            list_2.append(word)
        if (word.isdigit()):
            sli=int(word)
    print(''.join(list_2[0:sli]))
if __name__ == '__main__':
    main()
