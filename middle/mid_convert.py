from back.gp import *
import eel


@eel.expose
def count_up_gp_py(summa_iska):
    return gosposhlina(summa_iska)


@eel.expose
def fill_the_form_py(summa_iska, sud, otvetchik):
    return zayava_for_event(summa_iska, sud, otvetchik)


@eel.expose
def open_url_py(court):
    return open_url(court)