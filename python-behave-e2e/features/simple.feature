Feature: Turn Manager

Scenario: Show player creation
    Given character creation is "hidden"
    When user toggles character creation
    Then character form is "shown"

Scenario: Hide player creation
    Given character creation is "shown"
    When user toggles character creation
    Then character form is "hidden"