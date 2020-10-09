from django.db import models


class director(models.Model):
    name = models.CharField(max_length=150)
    desc = models.TextField()

    def __str__(self):
        return self.name


class movieData(models.Model):
    movieName = models.CharField(max_length=250)
    description = models.TextField()
    directorName = models.ForeignKey(director, on_delete=models.CASCADE)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.movieName


class timeSlots(models.Model):
    startTime = models.CharField(max_length=10)
    endTime = models.CharField(max_length=10)

    def __str__(self):
        return self.startTime + '-' + self.endTime


class shows(models.Model):
    movie = models.ForeignKey(movieData, on_delete=models.CASCADE)
    timeSlots = models.ForeignKey(timeSlots, on_delete=models.CASCADE)
    ticketPrice = models.IntegerField(default=0)
    totalTickets = models.IntegerField(default=0)
    ticketsSold = models.IntegerField(default=0)

    def __str__(self):
        return self.movie.movieName + ' ' + self.timeSlots.__str__()


class tickets(models.Model):
    movieShow = models.ForeignKey(shows, on_delete=models.CASCADE)
    nTickets = models.IntegerField(default=1)
