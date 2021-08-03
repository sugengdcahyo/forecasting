from plotly import graph_objects as go

class Figures:
    def __init__(self, dataframe, *args, **kwargs):
        self.dataframe = dataframe
    
    def candleStick(self):
        fig = go.Figure(
            data=[go.Candlestick(
                x=self.dataframe['Date'],
                open=self.dataframe['Open'],
                high=self.dataframe['High'],
                low=self.dataframe['Low'],
                close=self.dataframe['Price']
            )]
        )

        fig.update_layout(
            autosize=True,
            height=800,
            xaxis_rangeslider_visible=False
        )

        fig.show(config={'scrollZoom': True})
        
    def lineCharts(self):
        pass