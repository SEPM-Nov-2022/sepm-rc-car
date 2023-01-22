Feature: Analytics for the toy producer

    Scenario: As the toy producer, I want to know how the toy is used
        Given the server is online
        And the app is connected to the race car and the race car is charged
        When the app is online
        Then the server is notified