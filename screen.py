def screen_tag(tag,t_tag,bool):
    if bool == True:
        return set(t_tag) <= set(tag)
    else:
        for i in t_tag:
            if i in tag:
                return False
        return True