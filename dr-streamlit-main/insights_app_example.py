from datarobot import Client
from datarobot.client import set_client
from dr_streamlit import multiclass_dropdown_menu, derived_features_chart, text_feature_dropdown_menu, project_model_dropdown, wordcloud_chart


if __name__ == '__main__':
    c = Client(
        token='',
        endpoint='https://app.datarobot.com/api/v2/'
    )
    set_client(c)

    project_id = ""
    model_id = project_model_dropdown(project_id)
    selected_class = multiclass_dropdown_menu(project_id, model_id)
    selected_feature = text_feature_dropdown_menu(project_id)
    wordcloud_chart(
        project_id=project_id,
        model_id=model_id,
        specified_class=selected_class,
        selected_feature=selected_feature,
    )
    derived_features_chart(
        project_id=project_id,
        model_id=model_id,
        selected_class=selected_class
    )