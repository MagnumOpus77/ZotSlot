import mechanicalsoup
import re

# browser.form.print_summary()      prints out all of the form options


# codes to try: 4020, 27600, 05090
# Wait list: 35510, 
# n/a wait list: 35750
# Enrollement with '/': 30400, 81100
# three teachers: 35750------


def return_data(course_c):
    url = "https://www.reg.uci.edu/perl/WebSoc"
    browser = mechanicalsoup.StatefulBrowser()
    browser.open(url)
    browser.select_form('form[action="https://www.reg.uci.edu/perl/WebSoc"]')

    # try:
    print(f"THIS IS THE CC: {course_c}")
    browser["CourseCodes"] = course_c
    #browser.launch_browser()
    response = browser.submit_selected()

    print('>>>>>>>>')
    #print(response.text)

    print()
    print("------------")
    tds = response.soup.find_all('td')
    #print(tds)


    important_txt = re.findall('nowrap="nowrap">(\d+)</td>', str(tds))      # list
    print()

    dic = {}

    #print(len(important_txt))
    class_abr = re.findall('<tr bgcolor="#fff0ff" valign="top"><td class="CourseTitle" colspan="17" nowrap="nowrap">&nbsp; ((?:\D|&)+) &nbsp; (\d+[A-Z]?)', response.text)[0]
    class_abr = " ".join(class_abr)
    if "amp;" in class_abr:
        class_abr = class_abr.replace("amp;", "")
    dic["class_abr"] = class_abr
    
    dic["class_name"] = re.findall('<font face="sans-serif"><b>((?:\w| |&amp;)+)</b></font>', response.text)[0]
    frac_enrollment = re.findall('nowrap="nowrap">(\d+) / (\d+)</td>', str(tds))
    waitlist_option = re.findall('nowrap="nowrap">(n/a)</td>', str(tds))
    dic["class_type"] = re.findall('nowrap="nowrap">(Dis|Lec|Lab)</td>', str(tds))[0]

    instructor = re.findall('nowrap="nowrap">(STAFF)</td>', str(tds))
    # if there's multiple instructors
    if not instructor:
        istr = '(?:(?:<br/>|<br />)([A-Z\|-]+, [A-Z\|-].))?(?:<br />STAFF)?'      # each teacher is a group
        instructor = re.findall(f'nowrap="nowrap">([A-Z\|-]+, [A-Z\|-].){istr * 5}(?:<br/>|<br />)?</td>', response.text)[0]        # can capture up to 6 teachers
        print(instructor)
    dic["instructor_list"] = " ".join([i for i in instructor if i != ''])

    class_time = re.findall('nowrap="nowrap">(?:((?:M|W|F|Tu|Th|Sa|Su)+)   +(1?\d:\d\d- *1?\d:\d\dp?)|[  ]*TBA)', str(tds))[0]
    if class_time != ('',''):
        class_time = " ".join(class_time)
        dic["class_time"] = class_time
    else:
        dic["class_time"] = "TBA"

    dic["status"] = re.findall('(?:<font color="\D+">|nowrap="nowrap">)(OPEN|FULL|Waitl|NewOnly)(?:</td>|</font>)', str(tds))[0]


    if frac_enrollment:
        dic["course_code"] = important_txt[0]
        dic["units"] = important_txt[1]
        dic["max_capacity"] = important_txt[2]
        dic["enrolled"] = frac_enrollment[0][0]        # group 0

        if waitlist_option:
            dic["waitlisted"] = 'n/a'
            dic["requested"] = important_txt[3]
            dic['reserved_new'] = important_txt[4]
        else:
            dic["waitlisted"] = important_txt[3]
            dic["requested"] = important_txt[4]
            dic['reserved_new'] = important_txt[5]

    else:
        dic["course_code"] = important_txt[0]      
        dic["units"] = important_txt[1]
        dic["max_capacity"] = important_txt[2]
        dic["enrolled"] = important_txt[3]
        
        if waitlist_option:
            dic["waitlisted"] = 'n/a'
            dic["requested"] = important_txt[4]
            dic['reserved_new'] = important_txt[5]
        else:
            dic["waitlisted"] = important_txt[4]
            dic["requested"] = important_txt[5]
            dic['reserved_new'] = important_txt[6]



    print(f"Class Abreviation: {dic['class_abr']}")
    print(f"Class name: {dic['class_name']}")
    print(f"Instructor(s): {dic['instructor_list']}")
    print(f"Time: {dic['class_time']}")
    print("Course Code:", int(dic['course_code']))
    print("Class Type:", dic['class_type'])
    print("Units:", int(dic['units']))
    print("Max:", int(dic['max_capacity']))
    print("Enrolled:", int(dic['enrolled']))
    print("Waitlisted:", dic['waitlisted'])
    print("Requested:", int(dic['requested']))
    print("Reserved for New:", int(dic['reserved_new']))
    print("Status:", dic['status'])
    print('=====================')
    print()

    return dic


# return_data("27600")


# dic["class_abr"] = class_abr
# dic["class_name"] = class_name
# dic["instructor_list"] = instructor_list
# dic["class_time"] = class_time
# dic['course_code'] = course_code
# dic['class_type'] = class_type
# dic['units'] = units
# dic['max_capacity'] = max_capacity
# dic['enrolled'] = enrolled
# dic['waitlisted'] = waitlisted
# dic['requested'] = requested
# dic['reserved_new'] = reserved_new
# dic['status'] = status
