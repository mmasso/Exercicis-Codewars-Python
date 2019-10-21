def smallest_elements(ll,n):
    nn=len(ll)-n
    ll.reverse()
    for x in range(nn):
        ll=ll[:ll.index(max(ll))]+ll[ll.index(max(ll))+1:]
    ll.reverse()
    return ll