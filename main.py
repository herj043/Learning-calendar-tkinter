# Please note. You won't be able to insert a lot of code and files, otherwise that will destroy your performance in replit for example your program file "Learning tkinter".



# Python program to display calendar of
# given month of the year
   
# import module
import calendar as cal
   
yy = 2022
mm = 6
dd = 19
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satuday", "Sunday"]
day = cal.weekday(yy, mm, dd)

# display the calendar
print(cal.month(yy, mm))
print(str(days[day]) + ": " + str(dd))