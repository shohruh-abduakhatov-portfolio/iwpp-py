from src.in_warehouse_product_picker import main as iwpp_main


distance = {
    '3.0_0.75': {'3.0_0.75': {'distance': 0, 'direction': 0}, '3.0_3.25': {'distance': 7.0, 'direction': 2},
                 '3.0_5.75': {'distance': 9.5, 'direction': 2}, '3.0_8.25': {'distance': 12.0, 'direction': 2},
                 '3.0_10.75': {'distance': 14.5, 'direction': 2},
                 '3.0_13.25': {'distance': 17.0, 'direction': 2},
                 '7.5_0.75': {'distance': 0.0, 'direction': -2}, '7.5_3.25': {'distance': 2.5, 'direction': -2},
                 '7.5_5.75': {'distance': 5.0, 'direction': -2}, '7.5_8.25': {'distance': 7.5, 'direction': -2},
                 '7.5_10.75': {'distance': 10.0, 'direction': -2},
                 '7.5_13.25': {'distance': 12.5, 'direction': -2},
                 '12.0_0.75': {'distance': 4.5, 'direction': -2},
                 '12.0_3.25': {'distance': 7.0, 'direction': -2},
                 '12.0_5.75': {'distance': 9.5, 'direction': -2},
                 '12.0_8.25': {'distance': 12.0, 'direction': -2},
                 '12.0_10.75': {'distance': 14.5, 'direction': -2},
                 '12.0_13.25': {'distance': 17.0, 'direction': -2},
                 '7_14.5': {'distance': 14.25, 'direction': -2}},
    '3.0_3.25': {'3.0_0.75': {'distance': 7.0, 'direction': 2}, '3.0_3.25': {'distance': 0, 'direction': 0},
                 '3.0_5.75': {'distance': 7.0, 'direction': 2}, '3.0_8.25': {'distance': 9.5, 'direction': 2},
                 '3.0_10.75': {'distance': 12.0, 'direction': 2},
                 '3.0_13.25': {'distance': 14.5, 'direction': 2},
                 '7.5_0.75': {'distance': 2.5, 'direction': -2}, '7.5_3.25': {'distance': 0.0, 'direction': -2},
                 '7.5_5.75': {'distance': 2.5, 'direction': -2}, '7.5_8.25': {'distance': 5.0, 'direction': -2},
                 '7.5_10.75': {'distance': 7.5, 'direction': -2},
                 '7.5_13.25': {'distance': 10.0, 'direction': -2},
                 '12.0_0.75': {'distance': 7.0, 'direction': -2},
                 '12.0_3.25': {'distance': 4.5, 'direction': -2},
                 '12.0_5.75': {'distance': 7.0, 'direction': -2},
                 '12.0_8.25': {'distance': 9.5, 'direction': -2},
                 '12.0_10.75': {'distance': 12.0, 'direction': -2},
                 '12.0_13.25': {'distance': 14.5, 'direction': -2},
                 '7_14.5': {'distance': 11.75, 'direction': -2}},
    '3.0_5.75': {'3.0_0.75': {'distance': 9.5, 'direction': 2}, '3.0_3.25': {'distance': 7.0, 'direction': 2},
                 '3.0_5.75': {'distance': 0, 'direction': 0}, '3.0_8.25': {'distance': 7.0, 'direction': 2},
                 '3.0_10.75': {'distance': 9.5, 'direction': 2},
                 '3.0_13.25': {'distance': 12.0, 'direction': 2},
                 '7.5_0.75': {'distance': 5.0, 'direction': -2}, '7.5_3.25': {'distance': 2.5, 'direction': -2},
                 '7.5_5.75': {'distance': 0.0, 'direction': -2}, '7.5_8.25': {'distance': 2.5, 'direction': -2},
                 '7.5_10.75': {'distance': 5.0, 'direction': -2},
                 '7.5_13.25': {'distance': 7.5, 'direction': -2},
                 '12.0_0.75': {'distance': 9.5, 'direction': -2},
                 '12.0_3.25': {'distance': 7.0, 'direction': -2},
                 '12.0_5.75': {'distance': 4.5, 'direction': -2},
                 '12.0_8.25': {'distance': 7.0, 'direction': -2},
                 '12.0_10.75': {'distance': 9.5, 'direction': -2},
                 '12.0_13.25': {'distance': 12.0, 'direction': -2},
                 '7_14.5': {'distance': 9.25, 'direction': -2}},
    '3.0_8.25': {'3.0_0.75': {'distance': 12.0, 'direction': 2}, '3.0_3.25': {'distance': 9.5, 'direction': 2},
                 '3.0_5.75': {'distance': 7.0, 'direction': 2}, '3.0_8.25': {'distance': 0, 'direction': 0},
                 '3.0_10.75': {'distance': 7.0, 'direction': 2}, '3.0_13.25': {'distance': 9.5, 'direction': 2},
                 '7.5_0.75': {'distance': 7.5, 'direction': -2}, '7.5_3.25': {'distance': 5.0, 'direction': -2},
                 '7.5_5.75': {'distance': 2.5, 'direction': -2}, '7.5_8.25': {'distance': 0.0, 'direction': -2},
                 '7.5_10.75': {'distance': 2.5, 'direction': -2},
                 '7.5_13.25': {'distance': 5.0, 'direction': -2},
                 '12.0_0.75': {'distance': 12.0, 'direction': -2},
                 '12.0_3.25': {'distance': 9.5, 'direction': -2},
                 '12.0_5.75': {'distance': 7.0, 'direction': -2},
                 '12.0_8.25': {'distance': 4.5, 'direction': -2},
                 '12.0_10.75': {'distance': 7.0, 'direction': -2},
                 '12.0_13.25': {'distance': 9.5, 'direction': -2},
                 '7_14.5': {'distance': 6.75, 'direction': -2}},
    '3.0_10.75': {'3.0_0.75': {'distance': 14.5, 'direction': 2},
                  '3.0_3.25': {'distance': 12.0, 'direction': 2}, '3.0_5.75': {'distance': 9.5, 'direction': 2},
                  '3.0_8.25': {'distance': 7.0, 'direction': 2}, '3.0_10.75': {'distance': 0, 'direction': 0},
                  '3.0_13.25': {'distance': 7.0, 'direction': 2},
                  '7.5_0.75': {'distance': 10.0, 'direction': -2},
                  '7.5_3.25': {'distance': 7.5, 'direction': -2},
                  '7.5_5.75': {'distance': 5.0, 'direction': -2},
                  '7.5_8.25': {'distance': 2.5, 'direction': -2},
                  '7.5_10.75': {'distance': 0.0, 'direction': -2},
                  '7.5_13.25': {'distance': 2.5, 'direction': -2},
                  '12.0_0.75': {'distance': 14.5, 'direction': -2},
                  '12.0_3.25': {'distance': 12.0, 'direction': -2},
                  '12.0_5.75': {'distance': 9.5, 'direction': -2},
                  '12.0_8.25': {'distance': 7.0, 'direction': -2},
                  '12.0_10.75': {'distance': 4.5, 'direction': -2},
                  '12.0_13.25': {'distance': 7.0, 'direction': -2},
                  '7_14.5': {'distance': 4.25, 'direction': -2}},
    '3.0_13.25': {'3.0_0.75': {'distance': 17.0, 'direction': 2},
                  '3.0_3.25': {'distance': 14.5, 'direction': 2},
                  '3.0_5.75': {'distance': 12.0, 'direction': 2}, '3.0_8.25': {'distance': 9.5, 'direction': 2},
                  '3.0_10.75': {'distance': 7.0, 'direction': 2}, '3.0_13.25': {'distance': 0, 'direction': 0},
                  '7.5_0.75': {'distance': 12.5, 'direction': -2},
                  '7.5_3.25': {'distance': 10.0, 'direction': -2},
                  '7.5_5.75': {'distance': 7.5, 'direction': -2},
                  '7.5_8.25': {'distance': 5.0, 'direction': -2},
                  '7.5_10.75': {'distance': 2.5, 'direction': -2},
                  '7.5_13.25': {'distance': 0.0, 'direction': -2},
                  '12.0_0.75': {'distance': 17.0, 'direction': -2},
                  '12.0_3.25': {'distance': 14.5, 'direction': -2},
                  '12.0_5.75': {'distance': 12.0, 'direction': -2},
                  '12.0_8.25': {'distance': 9.5, 'direction': -2},
                  '12.0_10.75': {'distance': 7.0, 'direction': -2},
                  '12.0_13.25': {'distance': 4.5, 'direction': -2},
                  '7_14.5': {'distance': 1.75, 'direction': -2}},
    '7.5_0.75': {'3.0_0.75': {'distance': 0.0, 'direction': -2}, '3.0_3.25': {'distance': 2.5, 'direction': -2},
                 '3.0_5.75': {'distance': 5.0, 'direction': -2}, '3.0_8.25': {'distance': 7.5, 'direction': -2},
                 '3.0_10.75': {'distance': 10.0, 'direction': -2},
                 '3.0_13.25': {'distance': 12.5, 'direction': -2}, '7.5_0.75': {'distance': 0, 'direction': 0},
                 '7.5_3.25': {'distance': 7.0, 'direction': 2}, '7.5_5.75': {'distance': 9.5, 'direction': 2},
                 '7.5_8.25': {'distance': 12.0, 'direction': 2},
                 '7.5_10.75': {'distance': 14.5, 'direction': 2},
                 '7.5_13.25': {'distance': 17.0, 'direction': 2},
                 '12.0_0.75': {'distance': 0.0, 'direction': -2},
                 '12.0_3.25': {'distance': 2.5, 'direction': -2},
                 '12.0_5.75': {'distance': 5.0, 'direction': -2},
                 '12.0_8.25': {'distance': 7.5, 'direction': -2},
                 '12.0_10.75': {'distance': 10.0, 'direction': -2},
                 '12.0_13.25': {'distance': 12.5, 'direction': -2},
                 '7_14.5': {'distance': 17.75, 'direction': 2}},
    '7.5_3.25': {'3.0_0.75': {'distance': 2.5, 'direction': -2}, '3.0_3.25': {'distance': 0.0, 'direction': -2},
                 '3.0_5.75': {'distance': 2.5, 'direction': -2}, '3.0_8.25': {'distance': 5.0, 'direction': -2},
                 '3.0_10.75': {'distance': 7.5, 'direction': -2},
                 '3.0_13.25': {'distance': 10.0, 'direction': -2},
                 '7.5_0.75': {'distance': 7.0, 'direction': 2}, '7.5_3.25': {'distance': 0, 'direction': 0},
                 '7.5_5.75': {'distance': 7.0, 'direction': 2}, '7.5_8.25': {'distance': 9.5, 'direction': 2},
                 '7.5_10.75': {'distance': 12.0, 'direction': 2},
                 '7.5_13.25': {'distance': 14.5, 'direction': 2},
                 '12.0_0.75': {'distance': 2.5, 'direction': -2},
                 '12.0_3.25': {'distance': 0.0, 'direction': -2},
                 '12.0_5.75': {'distance': 2.5, 'direction': -2},
                 '12.0_8.25': {'distance': 5.0, 'direction': -2},
                 '12.0_10.75': {'distance': 7.5, 'direction': -2},
                 '12.0_13.25': {'distance': 10.0, 'direction': -2},
                 '7_14.5': {'distance': 15.25, 'direction': 2}},
    '7.5_5.75': {'3.0_0.75': {'distance': 5.0, 'direction': -2}, '3.0_3.25': {'distance': 2.5, 'direction': -2},
                 '3.0_5.75': {'distance': 0.0, 'direction': -2}, '3.0_8.25': {'distance': 2.5, 'direction': -2},
                 '3.0_10.75': {'distance': 5.0, 'direction': -2},
                 '3.0_13.25': {'distance': 7.5, 'direction': -2}, '7.5_0.75': {'distance': 9.5, 'direction': 2},
                 '7.5_3.25': {'distance': 7.0, 'direction': 2}, '7.5_5.75': {'distance': 0, 'direction': 0},
                 '7.5_8.25': {'distance': 7.0, 'direction': 2}, '7.5_10.75': {'distance': 9.5, 'direction': 2},
                 '7.5_13.25': {'distance': 12.0, 'direction': 2},
                 '12.0_0.75': {'distance': 5.0, 'direction': -2},
                 '12.0_3.25': {'distance': 2.5, 'direction': -2},
                 '12.0_5.75': {'distance': 0.0, 'direction': -2},
                 '12.0_8.25': {'distance': 2.5, 'direction': -2},
                 '12.0_10.75': {'distance': 5.0, 'direction': -2},
                 '12.0_13.25': {'distance': 7.5, 'direction': -2},
                 '7_14.5': {'distance': 12.75, 'direction': 2}},
    '7.5_8.25': {'3.0_0.75': {'distance': 7.5, 'direction': -2}, '3.0_3.25': {'distance': 5.0, 'direction': -2},
                 '3.0_5.75': {'distance': 2.5, 'direction': -2}, '3.0_8.25': {'distance': 0.0, 'direction': -2},
                 '3.0_10.75': {'distance': 2.5, 'direction': -2},
                 '3.0_13.25': {'distance': 5.0, 'direction': -2},
                 '7.5_0.75': {'distance': 12.0, 'direction': 2}, '7.5_3.25': {'distance': 9.5, 'direction': 2},
                 '7.5_5.75': {'distance': 7.0, 'direction': 2}, '7.5_8.25': {'distance': 0, 'direction': 0},
                 '7.5_10.75': {'distance': 7.0, 'direction': 2}, '7.5_13.25': {'distance': 9.5, 'direction': 2},
                 '12.0_0.75': {'distance': 7.5, 'direction': -2},
                 '12.0_3.25': {'distance': 5.0, 'direction': -2},
                 '12.0_5.75': {'distance': 2.5, 'direction': -2},
                 '12.0_8.25': {'distance': 0.0, 'direction': -2},
                 '12.0_10.75': {'distance': 2.5, 'direction': -2},
                 '12.0_13.25': {'distance': 5.0, 'direction': -2},
                 '7_14.5': {'distance': 10.25, 'direction': 2}},
    '7.5_10.75': {'3.0_0.75': {'distance': 10.0, 'direction': -2},
                  '3.0_3.25': {'distance': 7.5, 'direction': -2},
                  '3.0_5.75': {'distance': 5.0, 'direction': -2},
                  '3.0_8.25': {'distance': 2.5, 'direction': -2},
                  '3.0_10.75': {'distance': 0.0, 'direction': -2},
                  '3.0_13.25': {'distance': 2.5, 'direction': -2},
                  '7.5_0.75': {'distance': 14.5, 'direction': 2},
                  '7.5_3.25': {'distance': 12.0, 'direction': 2}, '7.5_5.75': {'distance': 9.5, 'direction': 2},
                  '7.5_8.25': {'distance': 7.0, 'direction': 2}, '7.5_10.75': {'distance': 0, 'direction': 0},
                  '7.5_13.25': {'distance': 7.0, 'direction': 2},
                  '12.0_0.75': {'distance': 10.0, 'direction': -2},
                  '12.0_3.25': {'distance': 7.5, 'direction': -2},
                  '12.0_5.75': {'distance': 5.0, 'direction': -2},
                  '12.0_8.25': {'distance': 2.5, 'direction': -2},
                  '12.0_10.75': {'distance': 0.0, 'direction': -2},
                  '12.0_13.25': {'distance': 2.5, 'direction': -2},
                  '7_14.5': {'distance': 7.75, 'direction': 2}},
    '7.5_13.25': {'3.0_0.75': {'distance': 12.5, 'direction': -2},
                  '3.0_3.25': {'distance': 10.0, 'direction': -2},
                  '3.0_5.75': {'distance': 7.5, 'direction': -2},
                  '3.0_8.25': {'distance': 5.0, 'direction': -2},
                  '3.0_10.75': {'distance': 2.5, 'direction': -2},
                  '3.0_13.25': {'distance': 0.0, 'direction': -2},
                  '7.5_0.75': {'distance': 17.0, 'direction': 2},
                  '7.5_3.25': {'distance': 14.5, 'direction': 2},
                  '7.5_5.75': {'distance': 12.0, 'direction': 2}, '7.5_8.25': {'distance': 9.5, 'direction': 2},
                  '7.5_10.75': {'distance': 7.0, 'direction': 2}, '7.5_13.25': {'distance': 0, 'direction': 0},
                  '12.0_0.75': {'distance': 12.5, 'direction': -2},
                  '12.0_3.25': {'distance': 10.0, 'direction': -2},
                  '12.0_5.75': {'distance': 7.5, 'direction': -2},
                  '12.0_8.25': {'distance': 5.0, 'direction': -2},
                  '12.0_10.75': {'distance': 2.5, 'direction': -2},
                  '12.0_13.25': {'distance': 0.0, 'direction': -2},
                  '7_14.5': {'distance': 5.25, 'direction': 2}},
    '12.0_0.75': {'3.0_0.75': {'distance': 4.5, 'direction': -2},
                  '3.0_3.25': {'distance': 7.0, 'direction': -2},
                  '3.0_5.75': {'distance': 9.5, 'direction': -2},
                  '3.0_8.25': {'distance': 12.0, 'direction': -2},
                  '3.0_10.75': {'distance': 14.5, 'direction': -2},
                  '3.0_13.25': {'distance': 17.0, 'direction': -2},
                  '7.5_0.75': {'distance': 0.0, 'direction': -2},
                  '7.5_3.25': {'distance': 2.5, 'direction': -2},
                  '7.5_5.75': {'distance': 5.0, 'direction': -2},
                  '7.5_8.25': {'distance': 7.5, 'direction': -2},
                  '7.5_10.75': {'distance': 10.0, 'direction': -2},
                  '7.5_13.25': {'distance': 12.5, 'direction': -2},
                  '12.0_0.75': {'distance': 0, 'direction': 0}, '12.0_3.25': {'distance': 7.0, 'direction': 2},
                  '12.0_5.75': {'distance': 9.5, 'direction': 2},
                  '12.0_8.25': {'distance': 12.0, 'direction': 2},
                  '12.0_10.75': {'distance': 14.5, 'direction': 2},
                  '12.0_13.25': {'distance': 17.0, 'direction': 2},
                  '7_14.5': {'distance': 14.25, 'direction': 2}},
    '12.0_3.25': {'3.0_0.75': {'distance': 7.0, 'direction': -2},
                  '3.0_3.25': {'distance': 4.5, 'direction': -2},
                  '3.0_5.75': {'distance': 7.0, 'direction': -2},
                  '3.0_8.25': {'distance': 9.5, 'direction': -2},
                  '3.0_10.75': {'distance': 12.0, 'direction': -2},
                  '3.0_13.25': {'distance': 14.5, 'direction': -2},
                  '7.5_0.75': {'distance': 2.5, 'direction': -2},
                  '7.5_3.25': {'distance': 0.0, 'direction': -2},
                  '7.5_5.75': {'distance': 2.5, 'direction': -2},
                  '7.5_8.25': {'distance': 5.0, 'direction': -2},
                  '7.5_10.75': {'distance': 7.5, 'direction': -2},
                  '7.5_13.25': {'distance': 10.0, 'direction': -2},
                  '12.0_0.75': {'distance': 7.0, 'direction': 2}, '12.0_3.25': {'distance': 0, 'direction': 0},
                  '12.0_5.75': {'distance': 7.0, 'direction': 2},
                  '12.0_8.25': {'distance': 9.5, 'direction': 2},
                  '12.0_10.75': {'distance': 12.0, 'direction': 2},
                  '12.0_13.25': {'distance': 14.5, 'direction': 2},
                  '7_14.5': {'distance': 11.75, 'direction': 2}},
    '12.0_5.75': {'3.0_0.75': {'distance': 9.5, 'direction': -2},
                  '3.0_3.25': {'distance': 7.0, 'direction': -2},
                  '3.0_5.75': {'distance': 4.5, 'direction': -2},
                  '3.0_8.25': {'distance': 7.0, 'direction': -2},
                  '3.0_10.75': {'distance': 9.5, 'direction': -2},
                  '3.0_13.25': {'distance': 12.0, 'direction': -2},
                  '7.5_0.75': {'distance': 5.0, 'direction': -2},
                  '7.5_3.25': {'distance': 2.5, 'direction': -2},
                  '7.5_5.75': {'distance': 0.0, 'direction': -2},
                  '7.5_8.25': {'distance': 2.5, 'direction': -2},
                  '7.5_10.75': {'distance': 5.0, 'direction': -2},
                  '7.5_13.25': {'distance': 7.5, 'direction': -2},
                  '12.0_0.75': {'distance': 9.5, 'direction': 2},
                  '12.0_3.25': {'distance': 7.0, 'direction': 2}, '12.0_5.75': {'distance': 0, 'direction': 0},
                  '12.0_8.25': {'distance': 7.0, 'direction': 2},
                  '12.0_10.75': {'distance': 9.5, 'direction': 2},
                  '12.0_13.25': {'distance': 12.0, 'direction': 2},
                  '7_14.5': {'distance': 9.25, 'direction': 2}},
    '12.0_8.25': {'3.0_0.75': {'distance': 12.0, 'direction': -2},
                  '3.0_3.25': {'distance': 9.5, 'direction': -2},
                  '3.0_5.75': {'distance': 7.0, 'direction': -2},
                  '3.0_8.25': {'distance': 4.5, 'direction': -2},
                  '3.0_10.75': {'distance': 7.0, 'direction': -2},
                  '3.0_13.25': {'distance': 9.5, 'direction': -2},
                  '7.5_0.75': {'distance': 7.5, 'direction': -2},
                  '7.5_3.25': {'distance': 5.0, 'direction': -2},
                  '7.5_5.75': {'distance': 2.5, 'direction': -2},
                  '7.5_8.25': {'distance': 0.0, 'direction': -2},
                  '7.5_10.75': {'distance': 2.5, 'direction': -2},
                  '7.5_13.25': {'distance': 5.0, 'direction': -2},
                  '12.0_0.75': {'distance': 12.0, 'direction': 2},
                  '12.0_3.25': {'distance': 9.5, 'direction': 2},
                  '12.0_5.75': {'distance': 7.0, 'direction': 2}, '12.0_8.25': {'distance': 0, 'direction': 0},
                  '12.0_10.75': {'distance': 7.0, 'direction': 2},
                  '12.0_13.25': {'distance': 9.5, 'direction': 2},
                  '7_14.5': {'distance': 6.75, 'direction': 2}},
    '12.0_10.75': {'3.0_0.75': {'distance': 14.5, 'direction': -2},
                   '3.0_3.25': {'distance': 12.0, 'direction': -2},
                   '3.0_5.75': {'distance': 9.5, 'direction': -2},
                   '3.0_8.25': {'distance': 7.0, 'direction': -2},
                   '3.0_10.75': {'distance': 4.5, 'direction': -2},
                   '3.0_13.25': {'distance': 7.0, 'direction': -2},
                   '7.5_0.75': {'distance': 10.0, 'direction': -2},
                   '7.5_3.25': {'distance': 7.5, 'direction': -2},
                   '7.5_5.75': {'distance': 5.0, 'direction': -2},
                   '7.5_8.25': {'distance': 2.5, 'direction': -2},
                   '7.5_10.75': {'distance': 0.0, 'direction': -2},
                   '7.5_13.25': {'distance': 2.5, 'direction': -2},
                   '12.0_0.75': {'distance': 14.5, 'direction': 2},
                   '12.0_3.25': {'distance': 12.0, 'direction': 2},
                   '12.0_5.75': {'distance': 9.5, 'direction': 2},
                   '12.0_8.25': {'distance': 7.0, 'direction': 2},
                   '12.0_10.75': {'distance': 0, 'direction': 0},
                   '12.0_13.25': {'distance': 7.0, 'direction': 2},
                   '7_14.5': {'distance': 4.25, 'direction': 2}},
    '12.0_13.25': {'3.0_0.75': {'distance': 17.0, 'direction': -2},
                   '3.0_3.25': {'distance': 14.5, 'direction': -2},
                   '3.0_5.75': {'distance': 12.0, 'direction': -2},
                   '3.0_8.25': {'distance': 9.5, 'direction': -2},
                   '3.0_10.75': {'distance': 7.0, 'direction': -2},
                   '3.0_13.25': {'distance': 4.5, 'direction': -2},
                   '7.5_0.75': {'distance': 12.5, 'direction': -2},
                   '7.5_3.25': {'distance': 10.0, 'direction': -2},
                   '7.5_5.75': {'distance': 7.5, 'direction': -2},
                   '7.5_8.25': {'distance': 5.0, 'direction': -2},
                   '7.5_10.75': {'distance': 2.5, 'direction': -2},
                   '7.5_13.25': {'distance': 0.0, 'direction': -2},
                   '12.0_0.75': {'distance': 17.0, 'direction': 2},
                   '12.0_3.25': {'distance': 14.5, 'direction': 2},
                   '12.0_5.75': {'distance': 12.0, 'direction': 2},
                   '12.0_8.25': {'distance': 9.5, 'direction': 2},
                   '12.0_10.75': {'distance': 7.0, 'direction': 2},
                   '12.0_13.25': {'distance': 0, 'direction': 0}, '7_14.5': {'distance': 1.75, 'direction': 2}},
    '7_14.5': {'3.0_0.75': {'distance': 14.25, 'direction': -2},
               '3.0_3.25': {'distance': 11.75, 'direction': -2},
               '3.0_5.75': {'distance': 9.25, 'direction': -2}, '3.0_8.25': {'distance': 6.75, 'direction': -2},
               '3.0_10.75': {'distance': 4.25, 'direction': -2},
               '3.0_13.25': {'distance': 1.75, 'direction': -2},
               '7.5_0.75': {'distance': 17.75, 'direction': 2}, '7.5_3.25': {'distance': 15.25, 'direction': 2},
               '7.5_5.75': {'distance': 12.75, 'direction': 2}, '7.5_8.25': {'distance': 10.25, 'direction': 2},
               '7.5_10.75': {'distance': 7.75, 'direction': 2}, '7.5_13.25': {'distance': 5.25, 'direction': 2},
               '12.0_0.75': {'distance': 14.25, 'direction': 2},
               '12.0_3.25': {'distance': 11.75, 'direction': 2},
               '12.0_5.75': {'distance': 9.25, 'direction': 2}, '12.0_8.25': {'distance': 6.75, 'direction': 2},
               '12.0_10.75': {'distance': 4.25, 'direction': 2},
               '12.0_13.25': {'distance': 1.75, 'direction': 2}, '7_14.5': {'distance': 0, 'direction': 0}}}


# {
# 'num_carts': 1,
# 'locations': [
# 	(7, 14.5), # 0
# 	(3.0, 13.25), # 1
# 	(3.0, 10.75), # 2
# 	(3.0, 10.75), # 3
# 	(3.0, 13.25), # 4
# 	(3.0, 10.75), # 5
# 	(3.0, 10.75), # 6
# 	(3.0, 13.25), # 7
# 	(3.0, 13.25)] # 8
# }
#
#
# {
# 'by_vehicle': {
# 	'0': {
# 		'nodes': [0, 8, 7, 6, 5, 4, 3, 2, 1, 0],
# 		'distance': 38.25
# 	}
# },
# 'total_distance': 38.25,
# 'by_route': {
# 	'nodes': [[0, 8, 7, 6, 5, 4, 3, 2, 1, 0]],
# 	'distances': [38.25]}}


def main():
    num_carts = 1
    # locations = [(7, 14.5),  # packing zone
    #              (3.0, 13.25),  # 1
    #              (7.5, 10.75),  # 2
    #              (3.0, 10.75),  # 3
    #              (3.0, 13.25),  # 4
    #              (3.0, 10.75),  # 5
    #              (3.0, 10.75),  # 6
    #              (3.0, 13.25),  # 7
    #              (7.5, 13.25),  # 8
    #              (12.0, 13.25),  # 9
    #              (3.0, 13.25)]  # 10
    locations = [[7, 14.5], [3.0, 13.25], [3.0, 10.75]]


    res = iwpp_main(num_carts, locations, distance)
    print(res)


if __name__ == '__main__':
    main()