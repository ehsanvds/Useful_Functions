def multiplot(x1, y1, sample, vmin=None, vmax=None,
              cmap='jet', title='', sp=[]):
    """
    Plotting a 2D contour from three 1D arrays
    """
    val = np.reshape(sample, (len(x1),len(y1)))
    val = np.transpose(val)
    
    if not sp:
        ax = plt.axes(aspect='equal')
        plt.contourf(x1, y1, val, levels=101, vmin=vmin, vmax=vmax, cmap=cmap)
    else :
        ax = plt.subplot(sp[0],sp[1],sp[2], aspect='equal')
        plt.contourf(x1, y1, val, levels=101, vmin=vmin, vmax=vmax, cmap=cmap)
        
    textprop = {'fontsize':22, 'fontstyle':'italic', 'fontname':'serif'}
    plt.xlim([-1.4,4.8])
    plt.ylim([-1.6,1.6])
    plt.xlabel('x*', textprop)
    plt.ylabel('y*', textprop)
    plt.title(title, textprop)
