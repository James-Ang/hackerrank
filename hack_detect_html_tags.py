# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 12:08:19 2021

@author: James Ang
"""


def parse1():
    n = 9
    with open("html_tags.txt") as f:
        text = f.readlines()
        # print(text)
        for l in text:
            #print(l.replace("\n",""))
            #print(type(lines))
            
            lines = l.replace("\n","")
            # print(lines)
            
            if lines.startswith("<") and not lines.startswith("</"):
                print(f"Tag: {lines}")
            
            elif lines.startswith(" "):
                print(f"Attrib: {lines}")


from html.parser import HTMLParser

def parse2():   # FINAL Solution
    
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            # print("Encountered a start tag:", tag)
            print(tag)
            # print(attrs)
            for attr in attrs:
                print(f"-> {attr[0]} > {attr[1]}")
    
        # def handle_endtag(self, tag):
            # print("Encountered an end tag :", tag)
    
        #def handle_data(self, data):
         #   print("Encountered some data  :", data)
            
        # method to append the comment to the list comments.
        # def handle_comment(self, data):
            # global comments
            # comments.append(data)
            # print("Encountered some data  :", data)
            
    parser = MyHTMLParser()
    with open("html_tags.txt") as f:
        text = f.readlines()
        # print(text)
        for l in text:
    
            parser.feed(l)


if __name__ == '__main__':
    
    parse2()