CREATE DATABASE flightsDatabase;
use flightsDatabase;

CREATE TABLE flights (
  source VARCHAR(20),
  dest VARCHAR(20),
  departureDay INT,
  departureHour INT,
  duration INT,
  numberOfSeats INT,
  flightId INT,
  books INT,
  boughtTickets INT
);


