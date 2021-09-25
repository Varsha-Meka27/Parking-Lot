# Parking-Lot

We own a parking lot that can hold up to ‘n’ cars at any given point in time. Each slot is given a number starting at one increasing with increasing distance from the entry point in steps of one. We want to create an automated ticketing system that allows our customers to use our parking lot without human intervention.

When a car enters the parking lot, we want to have a ticket issued to the driver. The ticket issuing process includes:- 
We are taking note of the number written on the vehicle registration plate and the age of the driver of the car.
And we are allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are kind enough to always park in the slots allocated to them).

The customer should be allocated a parking slot that is nearest to the entry. At the exit, the customer returns the ticket, marking the slot they were using as being available.

![Process](https://user-images.githubusercontent.com/80398182/134773238-4b85a2bb-dc35-4d8d-b359-acc2263a0d84.png)
