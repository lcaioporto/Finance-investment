import plotly.express as px
from plotly.io import to_html

class Utils():
    @staticmethod
    def get_plotly_html(
        x_data: list, y_data: list, title: str, x_label: str, y_label: str,
        highlight_x: float = None, highlight_y: float = None
        ) -> None:
        fig = px.line(x=x_data, y=y_data, title=title, template='plotly_dark')
        if highlight_x is not None and highlight_y is not None:
            print(f'Adding scatter at position ({highlight_x, highlight_y})')
            fig.add_scatter(
                x=[highlight_x], y=[highlight_y], name='Desired value',
                marker=dict(
                    color='red',
                    size=10
                ),
            )
        fig.update_xaxes(title_text=x_label)
        fig.update_yaxes(title_text=y_label)
        return to_html(fig, full_html=False)
    
    @staticmethod
    def format_number(value: float) -> str:
        return '{:,.2f}'.format(value).replace(',', 'X').replace('.', ',').replace('X', '.')