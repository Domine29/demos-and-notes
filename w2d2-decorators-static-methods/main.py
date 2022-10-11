def WidgetMakerMaker(widget_color):
    
    def WidgetMaker(name):
        return{
            'type': 'widget',
            'color': widget_color,
            'name' : name
        }

    return WidgetMaker

redWidgetMaker = WidgetMakerMaker('red')

red_widget = redWidgetMaker('name1')
another_red_one = redWidgetMaker('name2')


print(red_widget)
print(another_red_one)

blue_widget_maker = WidgetMakerMaker('blue')
# blue_widget = blue_widget_maker()

print(blue_widget)

