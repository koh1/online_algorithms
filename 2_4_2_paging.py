#-*- coding: utf-8 -*-
import numpy as np

class PageCache:
    def __init__(self, size):
        self.size = size
        self.page_mngr = {}
        self.page_marked = {}
        self.page_unmarked = {}
        self.page_access = []

    def mark(self, l):
        t = 0
        miss_hits = 0
        for e in l:
            if self.page_mngr.has_key(e):
                if self.page_marked.has_key(e):
                    pass
                else:
                    self.page_unmarked.pop(e)
                    self.page_marked[e] = True
            else:
                miss_hits += 1
                if len(self.page_mngr) >= self.size:
                    if len(self.page_unmarked) == 0:
                        for k in self.page_marked.keys():
                            self.page_marked.pop(k)
                            self.page_unmarked[k] = True

                    ## MARKの無いCache Pageからランダムに選択して削除する
                    target = self.page_unmarked.keys()[np.random.randint(0, len(self.page_unmarked))]
                    self.page_mngr.pop(target)
                    self.page_unmarked.pop(target)

                self.page_mngr[e] = True
                self.page_unmarked[e] = True
            t += 1
        return miss_hits

    def lru(self, l):
        pass

    def adversary(self, l):
        r = list()
        return r

    def obl_adversary(self, l):
        r = list()
        return r

    def offline(self, l):
        t = 0
        miss_hits = 0
        for e in l:
            if self.page_mngr.has_key(e):
                if self.page_marked.has_key(e):
                    pass
                else:
                    self.page_unmarked.pop(e)
                    self.page_marked[e] = True

            else:
                miss_hits += 1
                if len(self.page_mngr) >= self.size:
                    
                    ## 最も先にアクセスされるPageを削除する
                    target_page = ''
                    target_page_t = -1

                    for p in self.page_mngr.keys():
                        local_target = ''
                        local_target_t = -1
                        tt = t + 1
                        for a in l[t+1:]:
                            if p == a:
                                local_target = a
                                local_target_t = tt
                            tt += 1
                        
                        if local_target_t == -1 or target_page_t < local_target_t:
                            target_page = p
                            target_page_t = local_target_t

                    self.page_mngr.pop(target_page)
                    if self.page_unmarked.has_key(target_page):
                        self.page_unmarked.pop(target_page)
                    else:
                        self.page_marked.pop(target_page)
                     
                self.page_mngr[e] = True
                self.page_unmarked[e] = True
            t += 1
        return miss_hits


    
    def online(self, l):
        pass

if __name__ == '__main__':
    cache = PageCache(3)
    page_access = np.random.randint(0, 5, 10)
    print "input: %s" % page_access
    print "MARK: %d" % cache.mark(page_access)
    print "OFF: %d" % cache.offline(page_access)
