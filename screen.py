def screen_tag(tag,t_tag,bool):
    if bool == True:
        print(set(t_tag),set(tag))
        return set(t_tag) <= set(tag)
    else:
        for i in t_tag:
            if i in tag:
                return False
        return True