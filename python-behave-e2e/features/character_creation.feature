Feature: Character Creation

@ui
Scenario: Show player creation
    Given character creation is "hidden"
    When user toggles character creation
    Then character form is "shown"

@ui
Scenario: Hide player creation
    Given character creation is "shown"
    When user toggles character creation
    Then character form is "hidden"