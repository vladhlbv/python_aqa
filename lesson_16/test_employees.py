from lesson_16.employees import TeamLead


class TestEmployee:

    def test_team_lead_attributes_present(self):
        """
        Creating a new instance of the class TeamLead.
        Checking if created instance has all listed attributes from the parent classes.
        """

        lead = TeamLead(name="Tony", salary=5000, department="DEV", programming_language="Python", team_size=5)

        assert hasattr(lead, 'name'), "Attribute name is not present"
        assert hasattr(lead, 'salary'), "Attribute salary is not present"
        assert hasattr(lead, 'department'), "Attribute department is not present"
        assert hasattr(lead, 'programming_language'), "Attribute programming_language is not present"
        assert hasattr(lead, 'team_size'), "Attribute team_size is not present"