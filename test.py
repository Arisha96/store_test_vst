from vstutils.tests import BaseTestCase


class StoreTestCase(BaseTestCase):
    def setUp(self):
        super(StoreTestCase, self).setUp()
        # init demo project
        self.initial_project = self.get_model_class('store_test_vst.Item').objects.create(name="StoreTest")

    def tearDown(self):
        super(StoreTestCase, self).tearDown()
        # remove it after test
        self.initial_project.delete()

    def test_get_post_items_endpoint(self):
        # Test checks that api returns valid values
        self.list_test('/api/v1/items/', 1)
        self.details_test(
            ["items", self.initial_project.id],
            name=self.initial_project.name
        )
        # Try to create new items and check list endpoint
        test_data = [
            {"name": f"TestItem_{i}",
             "description": f"TestDescr_{i}",
             "cost": 100,
             "cost_type": "RUB"
             }
            for i in range(3)
        ]
        id_list = self.mass_create("/api/v1/items/", test_data, *test_data[0].keys())
        self.list_test('/api/v1/items/', 1 + len(id_list))

    def test_get_post_properties_endpoint(self):
        test_data_item = [{
            "name": f"TestItemProps",
            "description": f"TestDescrProps",
            "cost": 100,
            "cost_type": "RUB"
        }]
        id_for_prop_list = self.mass_create("/api/v1/items/", test_data_item, *test_data_item[0].keys())[0]
        test_data = [
            {
                "name": f"TestProp_{i}",
                "description": f"DescrTestProp_{i}"
            }
            for i in range(3)
        ]
        # Try to create new props for item and check list endpoint
        id_list = self.mass_create(f"/api/v1/items/{id_for_prop_list}/properties/", test_data, *test_data[0].keys())
        self.list_test(f"/api/v1/items/{id_for_prop_list}/properties/", 1 + len(id_list))
        self.details_test(
            ["properties", self.initial_project.id],
            name=self.initial_project.name
        )

    def test_get_single_item_property_endpoint(self):
        test_data_item = [
            {"name": f"TestItem",
             "description": f"TestDescr",
             "cost": 100,
             "cost_type": "RUB"
             }
        ]
        id_list_item = self.mass_create("/api/v1/items/", test_data_item, *test_data_item[0].keys())
        self.list_test(f'/api/v1/items/{id_list_item[0]}/', 1)
        test_data_property = [
            {
                "name": f"TestProp_{i}",
                "description": f"DescrTestProp_{i}"
            }
            for i in range(3)
        ]
        # Try to create new props for item and check list endpoint
        id_list_prop = self.mass_create(f"/api/v1/items/{test_data_item[0]}/properties/",
                                        test_data_property, *test_data_property[0].keys())
        self.list_test(f'/api/v1/items/{id_list_item[0]}/properties/{id_list_prop[0]}/', 1)
