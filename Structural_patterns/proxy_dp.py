"""
Proxy design pattern

INTENT:
    Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object.
    A proxy controls access to the original object, allowing you to perform something either before or after the
    request gets through to the original object.
APPLICABILITY:
    *Lazy initialization (virtual proxy). This is when you have a heavyweight service object that wastes
        system resources by being always up, even though you only need it from time to time.
    *Access control (protection proxy). This is when you want only specific clients to be able to use the service object;
     for instance, when your objects are crucial parts of an operating system and clients are various launched applications (including malicious ones).
     *Local execution of a remote service (remote proxy). This is when the service object is located on a remote server.
     *Logging requests (logging proxy). This is when you want to keep a history of requests to the service object.
     *Caching request results (caching proxy). This is when you need to cache results of client requests and manage
      the life cycle of this cache, especially if results are quite large.
     *Smart reference. This is when you need to be able to dismiss a heavyweight object once there are no clients that use it.
PROS AND CONS:
    PROS:
        *You can control the service object without clients knowing about it.
        *You can manage the lifecycle of the service object when clients don’t care about it.
        *The proxy works even if the service object isn’t ready or is not available.
        *Open/Closed Principle. You can introduce new proxies without changing the service or clients.
    CONS:
        *The code may become more complicated since you need to introduce a lot of new classes.
        *The response from the service might get delayed.
USAGE:
    While the Proxy pattern isn’t a frequent guest in most Python applications, it’s still very handy in some
    special cases. It’s irreplaceable when you want to add some additional behaviors to an object of some
    existing class without changing the client code.
IDENTIFICATION:
    Proxies delegate all of the real work to some other object. Each proxy method should, in the end, refer to a service
    object unless the proxy is a subclass of a service.
"""


# Production access proxy - used to access control over the object
class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"The car was driven by {self.driver.name}")


class CarProxy:
    def __init__(self, driver):
        # initialize the same attributes
        self.driver = driver
        # we cam initialize the car directly here as well
        self._car = Car(self.driver)

    def drive(self):
        # Add some conditionals
        if self.driver.age >= 18:
            self._car.drive()
        else:
            print("Too young to drive")


def test_production_proxy():
    driver = Driver("Mark", 20)
    car = CarProxy(driver)
    car.drive()

    driver2 = Driver("Tom", 15)
    car2 = CarProxy(driver2)
    car2.drive()


# Virtual proxy - a proxy that appears to be the underlying object but it is in fact not
class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from file {self.filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")


class LaziBitmap():
    def __init__(self, filename):
        self.filename = filename
        # set the initial state of bitmap
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            # Only initialize it if it is not initialized already
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Finished drawing the image")


def test_virtual_proxy():
    # In this case the image is being initialized even if it is not being drawn
    image = Bitmap("image.png")
    draw_image(image)
    # In order to avoid this we can use the Virtual proxy and lazy initialization
    # Even if it is being drawn multiple time, the image is initialized only once
    image2 = LaziBitmap("image2.jpg")
    draw_image(image2)
    draw_image(image2)
    draw_image(image2)


if __name__ == '__main__':
    print("Production proxy:")
    test_production_proxy()

    print("Virtual proxy:")
    test_virtual_proxy()
