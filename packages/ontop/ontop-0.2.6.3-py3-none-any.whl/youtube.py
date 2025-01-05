
from media import *
from ontop_csv import *



def draw_songs_graph(data, title):
    formatter = FuncFormatter(millions)
    cmap = plt.get_cmap("tab20c")
    count = min(len(data), 5)
    x = np.arange(count)
    views = data.filter(axis=1, items=['views']).head(count).values.flatten()
    titles = data.filter(axis=1, items=['title']).head(count).values.flatten()
    titles = [get_display(titles[i]) for i in range(count)]

    colors = cmap(np.arange(count) * 4)
    fig, ax = plt.subplots()
    fig.subplots_adjust(top=1.2)
    ax.yaxis.set_major_formatter(formatter)

    handles = [plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(count)]
    plt.legend(handles, titles)
    ax.text(0, 1.15, get_display(title), transform=ax.transAxes, size=24, weight=600, ha='left', va='top')

    plt.bar(x, views, color=colors)
    plt.xticks(x, [None for i in range(count)])

    x1,x2,y1,y2 = plt.axis()
    plt.axis((x1,x2,y1 ,y2 * 1.5))

    plt.show()


def millions(x, pos):
    """The two args are the value and tick position"""
    return '%1.1fM' % x
    
    
    
    
    
    https://www.instagram.com/reel/DA6fa_vIPA6/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA==
    