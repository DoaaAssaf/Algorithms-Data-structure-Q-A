'''
Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''


s = "abcafetcerujy"


def lengthOfLongestSubstring(s):
    max_length = 0
    dic = {}
    max_str = ""
    string_length = 0
    string = ""
    for i in range(len(s)):
        if dic.get(s[i]) is None:
            print("+++++++++++++++++++")
            print("add ",s[i])
            dic[s[i]] = i
            string_length += 1
            string += s[i]
            print("string=", string)
            if i == len(s)-1:
                max_length = string_length
                max_str = string

        else:
            print("+++++++++++++++++++")
            print("add ",s[i])
            if string_length > max_length:
                max_length = string_length
                max_str = string
                print("max string = ", max_str)

            last_repeat = dic[s[i]]
            print("last repeat for ", s[i], " = ", dic[s[i]])
            new_start = last_repeat + 1
            finish_append_char = i
            string = ""
            for j in range(new_start, finish_append_char+1):
                string +=s[j]
            print("delete to ",s[i]," and the new string = ", string)
            string_length = len(string)
            dic[s[i]] = i
            print("the longest string = ", max_length)
    print("--------------------------------")
    print("the final string =", max_str)
    print("its length",max_length)

lengthOfLongestSubstring(s)