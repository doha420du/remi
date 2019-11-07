# -*- coding: utf-8 -*-
import remi
import remi.gui as gui
import cv2


class OpencvImageWidget(gui.Image):
    icon = "data:image/png;base64,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"
    @gui.decorate_constructor_parameter_types([str])
    def __init__(self, filename, **kwargs):
        self.app_instance = None
        super(OpencvImageWidget, self).__init__("/%s/get_image_data" % id(self), **kwargs)
        self.style.update({'position':'absolute','left':'10px','top':'10px','width':'200px','height':'180px'})
        self.img = cv2.imread(filename, 0)
        self.frame_index = 0
        self.set_image(filename)

    @gui.decorate_set_on_listener("(self, emitter, image_data_as_numpy_array)")
    @gui.decorate_event
    def set_image(self, filename):
        return self.set_image_data(cv2.imread(filename, cv2.IMREAD_COLOR)) #cv2.IMREAD_GRAYSCALE)#cv2.IMREAD_COLOR)

    @gui.decorate_set_on_listener("(self, emitter, image_data_as_numpy_array)")
    @gui.decorate_event
    def set_image_data(self, image_data_as_numpy_array):
        self.img = image_data_as_numpy_array
        self.update(self.app_instance)
        return (self.img,)

    def search_app_instance(self, node):
        if issubclass(node.__class__, remi.server.App):
            return node
        if not hasattr(node, "get_parent"):
            return None
        return self.search_app_instance(node.get_parent()) 

    def update(self, *args):
        if self.app_instance==None:
            self.app_instance = self.search_app_instance(self)
            if self.app_instance==None:
                return
        self.frame_index = self.frame_index + 1
        self.app_instance.execute_javascript("""
            url = '/%(id)s/get_image_data?index=%(frame_index)s';
            
            xhr = null;
            xhr = new XMLHttpRequest();
            xhr.open('GET', url, true);
            xhr.responseType = 'blob'
            xhr.onload = function(e){
                urlCreator = window.URL || window.webkitURL;
                urlCreator.revokeObjectURL(document.getElementById('%(id)s').src);
                imageUrl = urlCreator.createObjectURL(this.response);
                document.getElementById('%(id)s').src = imageUrl;
            }
            xhr.send();
            """ % {'id': id(self), 'frame_index':self.frame_index})

    def refresh(self, opencv_img=None):
        self.img = opencv_img
        self.update(self.app_instance)

    def get_image_data(self, index=0):
        try:
            ret, png = cv2.imencode('.png', self.img)
            if ret:
                headers = {'Content-type': 'image/png'}
                return [png.tostring(), headers]
        except:
            pass
        return None, None


class OpencvCropImageWidget(OpencvImageWidget, object):
    icon = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACsAAAAuCAYAAACxkOBzAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAADpwAAA6cBPJS5GAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAfBSURBVFiFzZlrbJPnFcd/r28JSZrYcZwYUmeBEHCcmqFFrGqraWojPm2akHaRtq6sVOs6pn5A2odVW1mptBYJtqoq6tbLNgmNy9AkKHSFFAoFAqKAktJyJwQnhISEtLYTX+PLe/YhyRvbsRMTcLu/5EjPeZ7nvD8dnec8lyir3NXC/6mSJkPp+x0D4cm2AUDR6TFZa74+qgzFvHeQZGKa3QBgstawfPPurwym9+xJvrHisZz95//wU8L9nml23UxOLfSwmCOYuXnXQKNDt3N33rjMYOepu/aZE3YlL/OctPIj+SW/lsd5XDbeleOBw/vwD/Rl7auutrFYDeG7ce3eYZv4Ly2yFZhaew/zLo3yUV5O/bd6ecTZSLT7So4RCvUL5lPcc4mxUPDeYOvlZIZlHHoh7Xk5jXquUGuvoSQemnHcCmcjvs7Mb+VWVtgoFVkHRzDn5bQsHgGgwWrB1zt9oaTKlgiTiMXy8psV9jPlJyQoSrPFKeG88sNZHcajEcxGPQA1tirGbl7X+rojp9g29Bv8iUHN1rSwnuEr5+cO62URO5Xt9PFtwljp5RG2KzvxUzerQ//ALezWSq1dGhtPhbOBXewYep6LwTYCySGt32QyIeH88taQq6Ofb7Fd+XdeTlJVXGEm8KUHs3k8ZZbYq3ir8wU6zHuJyxgAQvqmqRM1L98z1tm56AGrjT7/sNa2WiyM9XdpoNmkSH47ftbIjnCbM4adfEkvoFCCGavU8U31B5RJVU5nfdHPafNtZFGsnEdZrtkf4iE+5VOtrWZEUmGOsBd0bew3vIpPuTVt8GF5gwZ5lO8kfkWdLE/ra/f/nWO+twipXmLJBxERFEUBYOXilezp20PQkT03ZWLcbEpLg37ded4zvJgVFCCijHJB18Y/jD9nr+ElksQBOOh9jQ+9mwip3nE/C/vpuN6hzbNUWGgKNE05ymAbiOW3k2mwgkqbYRMhxTvrpJgS5hP9v/incTV7/es55vsbSZk6JUmJ0D6SvoG4Fbe2IUpGjl6NnEQlmT9sp34315X8dxOAG7rTnK7YgWqc/qHO4k5Gg6Nae+XSlVT0Tt9sEokEPVyg3f9u/rCXdfnt+5mSYgEHYEy3+xf52X9tv9YuKy3DFXaNN1LS4NbgLUarRjkzupNA8ovZYYUk3conc4IFoBh4kPQVoMBR5ShjsamS5da5yVz4Hr8HMQveeB+Hva/PDhsnQlQZnXHgrJoH2NNN/Uv72Xdpn9ZudbZS6alMy1mv6tUi/Vnwffqi52aGTUys6ntWxcRvUgoclsNadEvmleCKutJ2MK9MLeioGuCIb8vMsCrT7ztzkgJYScvJzOguMyxD1OywANfCx4kmAzPBzl428lbxBPCkMqL7hPMJwne0C+s0WJUkIdWXG1bI7yCRtyykVYfU6BYVFVFpmjqVZcICJCV7Wk7A3uenAyNgS2lnRHd+xXwSiQSBQAB/mT9vt7rxP/r7iTquBxivEBNKjW6Lu4Wuri66B7uJ2qJ5uywcrB5IPaClRNdoNBKLxRiIDIzneJ4qHCxAKVA21ZyMrsfj4dy5cwyFh3JOzSZllbtaUBQilfepfGVKILUyqvoqrvZEsFVVUeX9AmxhMKWvmaKgHp2a/a0riYhS7NXnd6icI7ACoojC85GYbm0sRriri+cCAb43VEzngvkcmqeTDjUoil4Dl2KT7ut5NHzZ7f7x4Pz5IQH52G6XYRDJ+IXKypJnliy5+qrL9XtmuB8WVG83N2+JlJaqk1BJEE9tbRrox1arfPjss3KyoUGSIIM1NZEPXK4jLRZL9keMAki/x+k8HDMY5G2XS9QUuBN2exrsGEj71q0SCgalbcMGuWyziYAcX7LkQsEpW2trrScbG6+EFEV2P/OMHNq2LQ3Wa7HEux0OXyrwR08+KZM6d+CAXDebJW40ypr6+u8WDLRlwYKS6w6HVwXZs2aNqKoqR3ftSoPtdThG/tLc/CdRFM12qrZWQsGgBty2YYOMgRxobp7bzSAfbXQ6XxKQ9qYm7eOZsOcXL+4BdKnRTYIcf+cdDTaRSMiRFStkwG4PAcp9f+QAWGIyOQFira2UlJZmHeMrKhoC1PfKy99k4iquA2IHD2pj9Ho9ypo1VN25U/KzurrWgsCaREoSgPGx3E/xwzpdL8BvL178o8fh0E4zFceOMeKbOiI+/PTTdNhsfL+8/BcFgTWIFHlMJhpmgO1R1cnHAnVfWdlfJ+0tw8N0bN2qjZs3bx7R+noa4/GWgsCGIXjbYsFeW5tzzJlAQLuhrrt0ab2nrs4P45cMOXIkfXAsRmU0WlMQ2BG4Yw4GGRkZydofKy6WXTdvnkgxpUXXduIEw7fH/4Hy+f79NFy7RnkwWFYQ2P54vL8uFMLT0ZG131deHgPSTt3rLl1af2Mid5f5fBzavJmD69ZRvHo1jlCIgYqK4azO7lUrKiubkwaDHHjqKa0MpZauroUL72Sb97rL9cpkGfOl1N8bDodvrdPZUhBYQBmuqhrzGwxycNUqOb5pk2xZu1aDPbt06eUc89Lq7m27PbzD5fpPy4IFJYUCBWCPy/WBqtNNO1kJyCG3+1CueW+43S+ecjrPv9LU9Du+ypPXn93uF047nRd6HA7/YHV1xFdZGfObzfE3m5tfm4u//wEhpcccTGhJQgAAAABJRU5ErkJggg=="
    @gui.decorate_constructor_parameter_types([int, int, int, int])
    def __init__(self, x, y, w, h, **kwargs):
        self.app_instance = None
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        super(OpencvCropImageWidget, self).__init__("/%s/get_image_data" % id(self), **kwargs)

    @gui.decorate_set_on_listener("(self, emitter, image_data_as_numpy_array)")
    @gui.decorate_event
    def crop(self, emitter, image_data_as_numpy_array):
        self.img = image_data_as_numpy_array[self.x:self.x+self.w, self.y:self.y+self.h]
        self.update(self.app_instance)
        return (self.img,)


class OpencvVideoWidget(OpencvImageWidget):
    icon = "data:image/png;base64,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"
    @gui.decorate_constructor_parameter_types([int])
    def __init__(self, video_source=0, **kwargs):
        super(OpencvVideoWidget, self).__init__("/%s/get_image_data" % id(self), **kwargs)
        self.capture = cv2.VideoCapture(video_source)
        self.frame_index = 0
        self.app_instance = None
        self.last_frame = None

    def search_app_instance(self, node):
        if issubclass(node.__class__, remi.server.App):
            return node
        if not hasattr(node, "get_parent"):
            return None
        return self.search_app_instance(node.get_parent()) 

    def update(self, *args):
        if self.app_instance==None:
            self.app_instance = self.search_app_instance(self)
            if self.app_instance==None:
                print("no app instance")
                return
        self.frame_index = self.frame_index + 1
        self.app_instance.execute_javascript("""
            var url = '/%(id)s/get_image_data?index=%(frame_index)s';
            var xhr = new XMLHttpRequest();
            xhr.open('GET', url, true);
            xhr.responseType = 'blob'
            xhr.onload = function(e){
                var urlCreator = window.URL || window.webkitURL;
                urlCreator.revokeObjectURL(document.getElementById('%(id)s').src);
                var imageUrl = urlCreator.createObjectURL(this.response);
                document.getElementById('%(id)s').src = imageUrl;
            }
            xhr.send();
            """ % {'id': id(self), 'frame_index':self.frame_index})

    @gui.decorate_set_on_listener("(self, emitter, image_data_as_numpy_array)")
    @gui.decorate_event
    def set_image_data(self, image_data_as_numpy_array):
        self.img = image_data_as_numpy_array
        return (self.img,)

    def get_image_data(self, index=0):
        ret, frame = self.capture.read()
        if ret:
            self.set_image_data(frame)
            ret, png = cv2.imencode('.png', frame)
            if ret:
                headers = {'Content-type': 'image/png'}
                # tostring is an alias to tobytes, which wasn't added till numpy 1.9
                return [png.tostring(), headers]
        return None, None