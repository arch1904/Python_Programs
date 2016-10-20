from hw6 import *

################################################
#   Test Cases
################################################

def test_sorted_matrix_search():
    assert sorted_matrix_search([[1,2,3],[8,11,16],[23,24,25]], 8) == (1,0)
    assert sorted_matrix_search([[1,2,3],[8,11,16],[23,24,25]], 20) == (-1,-1)
    assert sorted_matrix_search([[1, 2, 3], [8, 11, 16], [23, 24, 25]], 25) == (2, 2)
def test_arr_almost_product():
    assert array_almost_product([2,3,4,5]) == [60, 40, 30, 24]
    assert array_almost_product([3,6,9,-3,2,-2]) == [648, 324, 216, -648, 972, -972]
    assert array_almost_product([1,2,3,4,5])==[120,60,40,30,24]

def test_pascals_triangle():
    assert pascals_triangle(2)==[1,2,1]
    assert pascals_triangle(6) == [1,6,15,20,15,6,1]

def test_alive_people():
    assert alive_people(["1920: 80", "1940: 22", "1961: 10"]) == 1961
    assert alive_people(["2000: 46", "1990: 17", "1200: 97", "1995: 20"]) == 2000

def test_number_to_text():
    assert number_to_text(99)=='ninety nine'
    assert number_to_text(100)=='hundred'
    assert number_to_text(4) == 'four'
    assert number_to_text(13)=='thirteen'
    assert number_to_text(0)=='zero'
    assert number_to_text(30)=='thirty'

def test_rotate_matrix():
    assert rotate_matrix([[1,2],[3,4]]) == [[2,4],[1,3]]
    assert rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]) == [[3,6,9],[2,5,8],[1,4,7]]

def test_largest_sum_subarray():
    assert largest_sum_subarray([-8,-6,1,-4,3,4,6]) == [3,4,6]
    assert largest_sum_subarray([2,-8,7,-3,4,-20]) == [7,-3,4]
    assert largest_sum_subarray([-1,-2,-3,-4]) == [-1]
def test_string_my_one_true_love():
    assert string_my_one_true_love("abcbabcdcdda") == True 
    assert string_my_one_true_love("aaabbbcccddde") == True 
    assert string_my_one_true_love("aaabbbcccdddeeffgg") == False

def test_gene_manipulation():
    assert gene_manipulation("ATCGGATT") == 1
    assert gene_manipulation("ATCGAAAAATCG")==3
    assert gene_manipulation("ATCGGTCA")==0
    assert gene_manipulation("ACAGATACAGAT")==5

def test_longest_palindrome():
    assert longest_palindrome_substring("ABBAC") == "ABBA"
    assert longest_palindrome_substring("A") == "A"
    assert longest_palindrome_substring("AAAAAAABBB")== "AAAAAAA"
    assert longest_palindrome_substring("AbBa")=="AbBa"
    assert longest_palindrome_substring("12321")=="12321"

def test_longest_unique():
    assert longest_unique_substring("asdfawefABCDEFaabasfeasf") == "wefABCD"
    assert longest_unique_substring("AA") == "A"
    assert longest_unique_substring("zzAabcdefFgg")=="abcdef"
    assert longest_unique_substring("abcdefghijklmnopqrstuvwxyz")=="abcdefghijklmnopqrstuvwxyz"

def test_three_sum():
    assert three_sum([-1, 0, 1, 2, -1, -4], 0) == [[-1, 0, 1],[-1, -1, 2]]

def test_all():
    test_sorted_matrix_search()
    test_arr_almost_product()
    test_pascals_triangle()
    test_alive_people()
    test_number_to_text()
    test_rotate_matrix()
    test_largest_sum_subarray()
    test_string_my_one_true_love()
    test_gene_manipulation()
    test_longest_palindrome()
    test_longest_unique()
    test_three_sum()
    print 'All Tests Passed!'

test_all()
