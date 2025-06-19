# # our_class.py 모듈 가져와서 (import 구문 사용)
# # 선생님 이름과 학생 수를 출력하고
# # study() 함수와 lecture() 함수를 호출하고
# # # 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
# # # go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해보자!


# # import our_class

# # print(our_class.teacher, our_class.student_count)

# # our_class.study()
# # our_class.lecture()

# # menus = ['햄버거', '치킨', '피자', '짜장면', '짬뽕']

# # print(our_class.go_lunch(menus))


# # import를 많이 하게 되면 내가 가져온 변수가 어디서 쓰인 변수인지 헷갈릴 수 있다는 단점이 있다

# # from our_class import teacher, student_count, study, lecture, go_lunch

# # print(teacher, student_count)
# # study()
# # lecture()

# # menus = ['햄버거', '치킨', '피자', '짜장면', '짬뽕']
# # print(go_lunch(menus))

# # 3.패키지 내의 모듈 import
# import our_class_dir.official.official_module
# from our_class_dir.unofficial.unofficial_module import study, go_lunch

# # 선생님 이름과 학생 수를 출력하고
# print(our_class_dir.official.official_module.teacher)
# print(our_class_dir.official.official_module.student_count)

# # study() 함수와 lecture() 함수를 호출하고
# study()
# our_class_dir.official.official_module.lecture()

# # # 먹고 싶은 메뉴명이 5개 담긴 menus 배열을 만들어서
# menus = ['햄버거', '치킨', '피자', '짜장면', '짬뽕']

# # # go_lunch() 함수를 호출해 오늘의 점심 메뉴를 출력해보자!
# print(go_lunch(menus))


import team_module

print(f"안녕하세요, {team_module.company}입니다.")
print(team_module.introduce_manager())
print(team_module.introduce_developer())

