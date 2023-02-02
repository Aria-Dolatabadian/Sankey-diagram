import plotly.graph_objects as go
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "Black", width = 2),
      label = ["Gene 1", "Gene 2", "Gene 3", "Gene 4", "Gene 5", "Trait 1","Trait 2","Trait 3","Trait 4"],
      color = ["blue","aqua","aquamarine"," turquoise","cadetblue","rgb(255,223,148)","rgb(255,223,200)", "rgb(255,232,113)","rgb(255,204,204)"]
    ),
    link = dict(
        source=[0, 0, 0, 0,  1, 1, 1, 1,  2, 2,2,2,3,3,3,3,4,4,4,4],  # indices correspond to labels, eg A1, A2, A1, B1, ...
        target=[5, 6, 7, 8,  5, 6, 7, 8,  5, 6,7,8,5,6,7,8,5,6,7,8],
        value= [18, 14, 12, 18, 14, 12, 5,12,4,12,13,14,11,25,12,10,11,12,12,14,12,11,11,12,14],
        color= ["turquoise","turquoise","turquoise","turquoise",
                "#4994CE","#4994CE","#4994CE","#4994CE",
                "cadetblue","cadetblue","cadetblue","cadetblue",
                "blue","blue","blue","blue",
                " bisque"," bisque"," bisque","bisque"]
    ))])
fig.update_layout(title_text="Basic Sankey Diagram", font_size=15)
fig.show()
