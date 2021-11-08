def main():
    # cetak judul program
    print('program menentukan nilai terbesar dua bilangan')
 
    # input user
    a = int(input('masukan bilangan ke-1: '))
    b = int(input('masukan bilangan ke-2: '))
 
    # menenukan nilai terbesar
    if a > b:
        if a > b:
            maks = a
    else:
            maks = b
 
    print('Nilai yang terbesar adalah: %d' % maks)
         
if __name__=='__main__':
    main()
