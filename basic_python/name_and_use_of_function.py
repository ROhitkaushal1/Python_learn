'''NOTE-
if iterables in:
[]-then its list
{}-and its set, but if it contain key pairs then dictionary
()-then its tuples'''


#1#
#gives absolute value basically |x| (mod x)
#function name: abs()
#only has one argument
print("example of function 'abs()':")
print(abs(-4578))
print(abs(4+6j))
print("\n")

# #2#
# #works on list, tuple, dictionary, strings, sets also called iterable
# #returns true if all items/values in these iterables are true, if not then returns false
# #function name: all()
# #only has one argument which is a iterable
# print("example of function 'all()':")
# list=[True,False,False,0]
# print(all(list))
# list_1=[True, True, True,1]
# print(all(list_1))
# print("\n")

# #3#
# #works on all iterables
# #returns true if any of the item/value in iterable is true,retruns false if all values are false
# #function name: any()
# #only has one argument which is a iterable
# print("example of function 'any()':")
# List=[0,0,0,False]
# print(any(List))
# List_1=[0,1,1,True]
# print(any(List_1))
# print("\n")

# #4#
# #basically is used to change non-ascii characters into escape characters
# #non-ascii characters are the symbols, letters etc that are not included in ascii table
# #function name: ascii() 
# #only has one argument which is object(string, list, tuple etc) .
# print("example of function 'ascii()':")
# tuple=("cool","mole","clause","$#@€","y€p")
# print(ascii(tuple))
# print("\n")

# #5#
# #it gives the binary version of any integer given as input
# #it has a prefix "0b", which basically signifies it's a binary number
# #function name: bin()
# #only has one argument, which is a binary number
# print("example of function 'bin()':")
# print(bin(6))
# print("\n")

# #6#
# #returns the boolean value of a specified object
# #returns true unless object is empty, has empty brackets, false, 0 or 'None'
# #function name: bool()
# #only has one argument
# print("example of function 'bool()':")
# print(bool("yes"))
# print(bool())
# print("\n")

# #7#
# #is mutable,returns the object(list, tuple, string etc) in form of bytearray object
# #also used to create empty bytearray object of specified size.
# #function name: bytearray()
# #has 3 optional parameters named source, encoding and error
# #Source:used to intialize the array in multiple ways,
# # necessary to specify encoding if source is a string, if integer makes a empty string of specifies size
# #Encoding:is the encoding of string like utf-8 or utf-16 etc
# #Error:specifies what to do if encoding fails,error arguments are->
# '''
# 1. strict: raises exception
# 2. replace: replaces malformed data with a suitable replacement marker
# 3. ignore: ignores malformed data
# 4. xmlcharrefreplace: replaces with the appropriate XML characters reference(used only for encoding)
# 5. backslashreplace: replaces with backslashed escape sequences(used only for encoding)
# '''
# print("example of function 'byetarray(`source`, `encoding`, `error`)'")
# print(bytearray(5))#5 is source, which creates bytearray of size 5
# print(bytearray("example continue",'utf-16', 'ignore'))
# print("\n")

# #8#
# #is immutable, is same as bytearray()
# #function name: bytes()
# #also has 3 optional arguments: source, encoding, error
# print("example of function 'bytes()':")
# print(bytes(4))
# print("\n")

# #9#
# #returns true if the specified object is callable, otherwise returns false
# #function name: callable().
# #has only one parameter
# print("example of function: 'callable()':")
# print("example 1:")
# x=5
# def cal(x):
#     return x
# y=cal
# print(callable(cal))
# print("example 2")
# def Cal():
#     return x
# y_1=Cal
# print(callable(Cal))
# n=x*5
# print(callable(n))

# #10#
# #returns the integer in the form of specified unicode
# #function name: chr()
# #has one integer argument .
# print("example of function 'chr()':")
# print(chr(33))
# print(chr(65))
# print("\n")

# #11#
# #can convert a method/function into class method
# #class method are method that works on class unlike normal methods that needs no specific parameters
# #function name: classmethod()
# #has single parameter which is a function
# print("example of functon 'classmethod()':")
# class qwerty:
#     focus="workload"
#     def  click(talk):
#         print("their is a new thing called", talk.focus)

# qwerty.__new__=classmethod(qwerty.click)
# qwerty.__new__()
# print("\n")

# #12#
# #takes course code as input and returns a code objet that is ready to be executed
# #function name: compile()
# #has 5 parameters source, filename, mode, (flags, dont_inherit, optimize)<-optional
# '''
# #Source- can be a normal or byte string or an AST object
# #Filename- takes the name of file from the code but can be changed
# #Mode- has total 3 modes: exec, eval or single
#     exec: (execute) if it is a block of code with python statements, class and functions
#     eval: (evaluate) if course is a single expression
#     single:if source is a single interactive statement
# #Flags: default is 0, affects the compilations process
# #dont_inherit:default is False, is a boolean flag and determines flow of executions
# #optimize: controls the optimization level of compiler. defeult value of -1
# '''
# print("example of function 'compile()':")
# rep='x = 45\ny = 789\nxx = x + y\nprint("rit=",xx)'
# click= compile(rep, 'new', 'exec')#using mode: exec
# exec(click)

# x=54
# a=compile('x', 'dawg', 'single')#using mode: single
# exec(a)

# q=45
# s=compile('q==45','droid','eval')#using mode: eval
# print(eval(s))
# print("\n")

# #13#
# #returns the complex number from the given input 
# #function name: complex().
# #has two parameters real and imaginary
# print("example of function 'complex()':")
# print(complex(45,54))
# print("\n")

# #14#
# #used to delete spcefied attribute from specified object
# #function name: delattr()
# #has 2 parameters object and attribute
# print("example of function 'delatrr()':")
# class tract:
#     a="human"
#     b=45
#     c="Earth"
# delattr(tract,'b')#now tract has no attribute named b
# print(tract.b)#won't print b
# print(tract.a)#will still print a
# print("\n")

# #14#
# #is used to create a dictionary
# #function name: dict()
# #optional,can have multiple keyword arguments(literal infinity)
# print("example of function 'dict()':")
# d=dict(name="fool", age=None, desc="done")
# print(d["age"])
# print("\n")

# #15#
# #returns all properties and methods of specified object, inlcuding built-in properties which are default
# #function name: dir()
# #has one parameter
# print("example of function 'dir()':")
# class inter:
#     name="docker"
#     tender="Yes"
#     clause=True
# print(dir(inter))
# print("\n")

# #16#
# #returns a tuple contaning quotient and remainder
# #function name: divmod()
# #has 2 argument (1st is a dividend and 2nd is a divisor)
# print("example of function 'divmod()':")
# print(divmod(10,5))
# print("\n)

# #17#
# #takes a iterable and returns it as an enumerate object, also helps in easing the count process
# #function name:enumerate()
# #has 2 parameters [iterable,start] where start is 0 by default and acts as a index
# print("example of function 'enumerate()':")
# pit=('Bool','Pool','Cool','Tool','Wool','Fool','Rool','Dool')
# for p in enumerate(pit):
#     print(p)
# str="forgetting"
# print(list(enumerate(str)))
# print("\n")

# #18#
# #evaluates a specified expression and executes if it's a valid python statement
# #function name: eval()
# #has 3 parameters, 2 optional [expression, (golbal, local)optional]
# #global is a dictionary of global parameters and local is dictionary to local parameters.
# print("example of function 'eval()':")
# x='print("parameterised answer is", 45+78+57)'
# eval(x)
# print("/n")

# #19#
# #executes the specifies python code, accepts large blocks of code unlike eval() function which only accepts a single expression
# #function name: exec()
# #also has 3 parameters, 2 optional [object, (global, local)optional]
# print("example of function 'exec()':")
# x='test="yes"\nprint(test)'
# exec(x)
# print("\n")

# #20#
# #returns result after applying said function on the iterable
# #function name: filter() 
# #has 2 arguments [function, iterable]
# print("example of function 'filter()':")
# num=[45,87,54,59,48,21,85,41,81,96]
# def trial(x):
#     if x<60:
#         return False  
#     else:
#         return True
# work= filter(trial, num)
# for x in work:
#     print(x)
# print("\n")

# #21#
# #converts the given integer to a floating number 
# #function name: float()
# #has single parameter [value]
# print("example of function 'float':")
# print(float(45))
# print("\n")

# #22#
# #formats a specified value into a specified format
# #function name: format()
# #has 2 arguments [value, format]
# #(format) helps by formatting the value into given values:
# '''
# '<':left aligns
# '>':right aligns
# '^':center aligns
# '=':places the sign to left most position
# '+':indicates if result will be positive
# '-':use a minus sign for negative values only
# ' ':use a leading space for positive numbers
# ',':use a comma as a thousand separator(like 10,000)
# '_':use a underscore as a thousand separator
# 'b':binary format
# 'c':converts the value into the corresponding unicode character
# 'd':decimal format
# 'e':scientific format, with a lower case e
# 'E':scientific format, with a lower case E
# 'f':fix point number format
# 'F':fix point number format, upper case
# 'g':general format
# 'G':general format, (using a upper case E for scientific notations)
# 'o':octal format
# 'x':hex format, lower case
# 'X':hex format, upper case
# 'n':number format
# '%':percentage format
# '''
# print("example of function 'format()':")
# x=float('inf')
# print(format(x, 'F'))
# print(format(x,'f'))
# print(format(100000, ','))
# print(format(0.5,'%'))
# print("\n")

# #23#
# #function returns an unchngeable frozenset, basically a immutable set
# #function name: frozenset()
# #has 1 parameter [iterable]
# print("example of function 'frozenset()':")
# tree=frozenset(['mango','litchi', 'devdar', 'sandalwood'])
# print(tree)
# print("mango" in tree)
# print("need" in tree)
# print("\n")

# #24#
# #returns value of specified attribute from the specified object
# #function name: getattr() 
# #has 3 parameters, 1 optional [object, attribute, default] default can be used to write a msg if attribute does not exis
# print("example of function 'getattr()':")
# class msgs:
#     name='Null'
#     work='studying'
#     end='soon'
#     state='lapse'
# print(getattr(msgs, 'born', "doesn't exist"))
# print("\n")

# #25#
# #returns the global symbol table as a dictionary
# #symbol table contains necessary information about the current program
# #function name: globals()
# print("example of function 'global()':")
# print(globals())
# print("\n")

# #26#
# #returns True if specified object has the specified attribute,otherwise False
# #function name: hasattr()
# #has 2 parameters [object, attribute]
# print("example of function 'hasattr':")
# class goal:
#     name='Clobart'
#     age=88
#     world=1285
#     universe=548773812
#     intelligence='average according to species'
# x=hasattr(goal, 'species') #doesn't have attribute named species
# print(x)
# print("\n")

# #27#
# #returns the hash value of an object if it has one
# #hash value is an integer that is used to quickly compare dictionary keys.
# #function name: hash()
# #has one parameter [object]
# print("example of function 'hash()':")
# n=24.56
# print(hash(n))
# print("\n")

# #28#
# #executes the built-in help system
# #function name: help()
# #has no parameter
# print("example of function 'help()':")
# print(help())
# print("\n")

# #29#
# #converts specified number into a hexadecimal value with a prefix 0x
# #function name: hex()
# #has one parameter [number]
# print("example of function 'hex()':")
# print(hex(10))
# print(hex(13))
# print("\n")

# #30#
# #returns a unique ID for the specified object, as every object has its unique ID
# #ID is the object's memory address which will be different each time program is run
# #function name: id()
# #has 1 parameter [object]
# print("example of function 'id()':")
# x="torque can be removed"
# print(id(x))
# print("\n")

# #31#
# #this function allows user input
# #function name: input()
# #has one parameter which is a input [prompt]
# print("example of function 'input()':")
# x=input("enter if yes or no: ")
# if x=='y':
#     print("good")
# else:
#     print("doesnt exist")
# print("\n")

# #32#
# #converts the specified value into an integer number, used in cryptography
# #function name: int()
# #has 2 parameter [value, base], base represents number format, default value 10
# print("example of function 'int()':")
# x=int("hgx445jgjn54",36)
# print(x)
# print("\n")

# #33#
# #returns True if the specified object is specified type
# #if the type is tuple, returns True if object is one of any types in tuple
# #function name: isinstance()  
# #has 2 parameters [object,type]
# print("example of function 'isinstance()':")
# print(isinstance(45,int))
# print(isinstance(45,str))
# print(isinstance(45, (float, int, str, list, dict, tuple)))
# print("\n")

# #34#
# #returns True if the specified object is a subclass of the specified object
# #function name: issubclass()
# #has 2 parameter [object, subclass]
# print("example of function 'issubclass()':")
# class new:
#     world=1285
# class root(new):
#     name="Boot"
#     world=new
# x= issubclass(root, new)
# print(x, root.world, new.world)
# print("\n")

# #35#
# #returns an iterator object
# #function name: iter()
# #has 2 parameters,1 optional [object,(sentinel)]
# print("example of function 'iter()':")
# x=["bootable","processing","cancel"]
# print(iter(x))
# print("\n")

# #36#
# #returns the length of the object
# #function name: len()
# #has 1 argument [object]
# print("example of function 'len()':")
# a=['dock','rock','shock','crock','lock']
# print(len(a))
# print("\n")

# #37#
# #use to create a list object
# #function name: list()
# #has 1 parameter [iterable], which is optional
# print("example of function 'list()':")
# qw=list(('software','hardware','output','input','C.P.U'))
# print(qw)
# print("\n")

# #38#
# #returns the local symbol table as a dictionary
# #function name: locals()
# #has no parameter
# print("example of function 'locals()':")
# print(locals())
# print("\n")

# #39#
# #executes a specified function for each item in an iterable, item becomes a parameter for a function
# #basically fucntion is implemented on each value/itemetc individually inside the iterable
# #function name: map()
# #has 2 parameters [function, iterables]
# print("example of function 'map()':")
# def phonk(h):
#     return len(h)
# x=map(phonk, ('util','support','out','print'))
# print(x)
# print(tuple(x))
# print("\n")

# #40#
# #returns the items with the highest value, or the item with the highest value in an iterable
# #function name: max()
# #has one parameter [iterable]
# print("example of fucntion 'max()':")
# print(max(5,2,7,3,5,9))
# print("\n")

# #41#
# #returns a memory view object from a specified object
# #function name: memoryview()
# #has one parameter [object]
# #object is a bytes object or a bytearray object
# x=bytes(4)
# n=memoryview(x)
# print(x)
# print(n)

# #42#
# #returns the iten with the lowest value,or the item with the lowest value in an iterable
# #function name: min()
# #has 1 parameter [iterable]
# print("example of function 'min()':")
# print(min(45,78,65,98,21,74,37,79,89))
# print("\n)

# #43#
# #returns next item in an iterator, used with iter()
# #function name: next()
# #has 2 parameters, 1 optional [iterable,(default)]
# print("example of function 'next()':")
# cf=iter(["torque","power","electricity","current"])
# print(next(cf))
# print(next(cf))
# print("\n")

# #44#
# #returns an empty object
# #new properties and method can't be added in this object
# #these objects is the base of all classes, it holds teh built-in properties and methods which are default for all classes
# #function name: object()
# #no parameter
# print("example of fuinction 'object()':")
# hbh=object()
# print(type(hbh))
# print(dir(hbh))
# print("\n")

# #45#
# #converts an integer into an octal string,with prefix 0o
# #function name: oct()
# #has 1 parameter [int]
# print("example of fucntion 'octal()':")
# print(oct(45))
# print("\n")

# #46#
# #function opens a file and returns it as a file object.
# #function name: open()
# #has 2 parameters [file, mode]
# '''
# mode:defines which mode to open file in-
# "r"(read)-[default]opens file for reading,error if does not exist
# "a"(append)-open a file for appending,creates if does not exist
# "w"(write)-opens a file for writing,creates if does not exist
# "x"(create)-creates the specified file,returns error if file exist
# "t"(text)-[default] text mode
# "b"(binary)-binary mode(like images etc)
# '''
# print("example of function 'open()':")
# ui=open("test999", 'r')
# print(ui.read())
# print("\n")

# #47#
# #returns the number representing the unicode code of the specfied character
# #function name: ord()
# #has 1 parameter [character]
# print("example of function 'ord()':")
# print(ord("a"))#single character
# print("\n")

# #48#
# #returns the value of x to the power of y->[x^y]
# #if z is present, it givfes modulus to the answer of x and y[x^y%z]
# #function name: pow()
# #has 3 parameter,1 optional [x,y,(z)]
# print("example of function 'pow()':")
# print(pow(4,2,3))#4x4=16,remainder of 16 with 3 is 1 
# print("\n")

# #49#
# #prints specified message to the screen, can also prints fucntion too
# #basically gives output on screen
# #function name: print()
# #has 5 parameters, 4 optional [object,(sep),(end),(file),(flush)]
# '''
# object-can be multiple string, function etc
# sep='<anything>'-specifies how to separate various object, default is ' '
# end='<anything>'-specifies what to print at the end, default is '\n'
# file=default is sys.stdout, it is an object with a write method
# flush=default is False, it is a boolean which specifies if the output is True(flushed) or False(buffered)
# '''
# print("Writing","local","troop", sep='cool')
# print("Writing","local","troop", end="cool")

# #50#
# #used to create a special attribute called property
# #properties are used to encapsulate the access to object 
# #also to add some logic to the process such as computation, validation and access control
# #function name: property()
# #has 4 parameters, all optional [fget,fset,fdel,doc]
# '''
# fget-gets the value of attribute or shows the recorded value
# fset-set the value of attribute or edits the recorded value
# fdel-delete the attribute value, deletes the recorded value
# doc-string that contains the documentation for the attribute
# 'if no arguments given, returns base property attribute'
# '''
# print("example of function 'property()':")
# class data:
#     def __init__(self, name):
#         self._name=name
#     #getter function
#     def get_name(self):
#         print("getting name...")
#         return self._name
#     #setter function
#     def set_name(self, value):
#         print("changing name...")
#         self._name=value
#         print("name changed to: ", value)
#     #deleter function    
#     def del_name(self):
#         print("deleting name...")
#         del self._name
#         print("|ok, name deleted|")
#     name=property(get_name, set_name, del_name)

# chng=input("enter the new name: ")
# per=data(chng)
# per.name=chng
# while True:
#     ask=input("do you want to change the name again?(y/n) ")
#     if ask=="y" or ask=="Y" or ask=="Yes" or ask=="yes" or ask=="YES":
#         gn=input("enter the new name: ")
#         per.name=gn
#     elif ask=="n" or ask=="N" or ask=="No" or ask=="no" or ask=="NO":
#         dela=input("do you want to delete the name?(y/n) ")
#         if dela=="y" or ask=="Y" or ask=="Yes" or ask=="yes" or ask=="YES":
#             del per.name
#             break
#         elif dela=="n" or ask=="N" or ask=="No" or ask=="no" or ask=="NO":
#             print("Got it")
#             break
#         else:
#             print("error, system failed")
#             break
#     else:
#         print("error, system failed")
#         break

# print("\n)

# #51#
# #helps in loop statements
# #returns a sequence starting from 0 as default and increment by 1 till specified number
# #function name:  range()
# #has 3 parameters, 2 optional [(start),stop,(step)]
# print("example of fucntion 'range()':")
# a=30
# for n in range(30,0,-1):
#     print(a)
#     a-=1
# print("\n")

# #52#
# #returns the object's string representation, the representation is more "raw" like and sometimes hard to read
# #function name: repr()
# #has 1 parameter [object]
# print("example of function 'repr()':")
# print(repr("new object"))
# fd=200
# print(type(repr(fd)))
# lit=[1,2,3]
# print(type(lit))
# print(type(repr(lit)))

# #53#
# #rerurns a reversed iterator object, which can be used in loop statements
# #function name: reversed()
# #has 1 parameter [sequence]
# print("example of function 'reversed()':")
# reve=['avicii', 'claw', 'drain', 'center']
# ever=reversed(reve)
# print(ever)
# for n in ever:
#     print(n)
# print("\n")

# #54#
# #returns a float value of the number which is rounded of, number of decimals can be specified
# #function name: round()
# #has 2 parameters, 1 optional [number, (digits)]
# print("example of function 'round()':")
# print(round(2.3974617687,4))
# print("\n")

# #55#
# #creates a set object, it is unordered and values can have random order
# #function name: set()
# #has one parameter []
# print("example of fucntion 'set()':")
# st=set({'food','weapons', 'planets', 'others'})
# print(st)
# print("\n")

# #56#
# #function sets the value of the specified attribute of the specified object
# #function name: setattr()
# #has 2 parameter [object, attribute, value]
# print("example of function 'setattr()':")
# class ion:
#     name="David"
#     age="26"
#     country="India"
# setattr(ion, "planet", "Earth")
# print(ion.planet)
# print(ion.age)
# setattr(ion, "age", 35)
# print(ion.age)
# print("\n")

# #57#
# #returns a slice object, 
# #function name: slice()
# #has 3 parameters,2 optional [(start),end,(stop)]
# print("example of function 'slice()':")
# tup=('a','b','c','d','v','f','e','g')
# sli=slice(4)
# print(tup[sli])
# print("\n")

# #58#
# #returns the sorted list of iterable
# #if it's string then it is sorted in ascencing or descending as specified
# #If it's numbers then it is sorted numerically
# #function name: sorted()
# #has 3 parameters, 2 optional [iterable, (key), (reverse)]
# '''
# key- a fucntion can be specified and will execute it
# and decide the order according to it.
# reverse-decides how to sort ascending or descending,
# false for ascending and true for descending.
# '''
# print("example of function 'sorted()':")
# srt=[81,25,1,8,11,21,5,45,19,22,12,75,98,24]
# print(sorted(srt))
# srt_1=['ark','acro','aztec','air','abbot','adria']
# print(sorted(srt_1,reverse=True))
# print(sorted(srt_1,reverse=False))
# print("\n")

# #59#
# #converts a function into a static method
# #a static method can be accessed without creating or associating a instance to it
# #function name: staticmethod()
# #has 1 parameter [function]
# print("example of fucntion 'staticmethod()':")
# class iou:
#     def __init__(obj,a,b):
#         obj.a=a
#         obj.b=b
    
#     def add(a,b):
#         return a,b
#     def sub(obj):
#         return obj.a-obj.b
# iou.add=staticmethod(iou.add)

# print(iou.add(45,5))

# jock=iou(45,5)
# print(jock.sub())
# print("\n")

# #60#
# #converts the given value into a string
# #function name: str()
# #has 3 parameters, 2 optional [object, encoding, errors]
# '''
# encoding-default is UTF-8, is the encoding of object, can be changed
# errors-specifies what to do when decoding fails,sams as bytearray
# '''
# print("example of function 'str()':")
# print(str(b"byte",encoding='UTF-32'))
# print("\n")

# #61#
# #returns the sum of all items/values in an iterable
# #function name: sum()
# #has 2 parameters,1 optional [iterable, (extra)]
# '''extra is the value added to return value'''
# print("example of function 'sum()':")
# x=[4,52,4,51,4,51,2,545,1,55]
# print(sum(x,2))
# print("\n")

# #62#
# #is used to give access to methods and properties of parent and sibling class
# #can make a instance become parent class
# #function name: super()
# #no parameters
# print("example of function 'super()':")
# class prnt:
#     def __init__(self,rex):
#         self.main=rex
    
#     def msg(self):
#         print(self.main)
    
# class chld(prnt):
#     def __init__(self,rex):
#         super().__init__(rex)

# nxt=chld("goal is money, money is goal")
# nxt.msg()
# print("\n")

# #63#
# #creates a tuple
# #function name: tuple()
# #has 1 parameter [iterable]
# print("example of function 'tuple()':")
# print(tuple(('door','moor','cloud',
#              'scout','draken','acoustic','voila')))
# print("\n")

# #64#
# #returns the type of the object
# #function name: type()
# #has 3 parameters, 2 optional [object, bases, dict]
# print("example of function 'type()':")
# print(type("char"))
# print("\n")

# #65#
# #returns the __dict__ attrtibute,which contains the object's changeable attributes
# #function name: vars()
# #has 1 parameter [object]
# class verse:
#     name="someone"
#     works="yes"
#     age=78
#     planet="Earth"
# vro=print(vars(verse))


# #66#
# #returns a zip object
# #basically pairs 2 different iterators with first items being paired together, then second and so on
# #function name: zip()
# #has multiple iterators [iterator1, iterator2, iterator3]
# frs=['blue','red','yellow','purple','green','white']
# snd=['sky','blood','mustard','gum','grass','page']
# trd=['clear','shining','golden','elastic','touch','clean']
# zeep=zip(trd,frs,snd)
# print(list(zeep))
