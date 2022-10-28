 <!-- <h2>Hello my name is {{first_name |lower | capfirst}} and my family name is {{last_name | length}}</h2>
    <h2>{{some_list.1}}</h2>
    <h2>{{some_dic.inside_key}}</h2>
    <h2>{# this a coment#} here isde </h2> -->

    <ul>
        {% for k,v in some_dic.items%}
            
                <li>{{v}}</li>
            

        {% endfor%}
    </ul>


    USING FOR LOOP AND IF STATEMENET
    <ul>
 {% for num  in some_list %}
    {% if num == 2 %}
        <li>TWO</li>

     {% else %}
        <li>{{num}}</li>
    {% endif %}

 {% endfor %}


 {% if user_logged_in %}
    <h2>Welcome {{first_name}} </h2>

    {% endif%}



       my_var = {'first_name':'Anna', 'last_name':'Marible',
                'some_list':[1,2,3,4,5,6,7,8,9,10], 'user_logged_in': True
    }

</ul>



very  impoptant class 66 in order to inheritfrom a template as instructutingyour project 