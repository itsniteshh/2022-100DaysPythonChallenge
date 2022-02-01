def build_profile(fname, lname, **user_info):
    #building dictionary about user details
    print(type(user_info))
    user_info["first name"] = fname
    user_info["last name"] = lname
    return user_info

user_profile = build_profile('nitesh', 'jha',location='mumbai', field='coding')
print(user_profile)

