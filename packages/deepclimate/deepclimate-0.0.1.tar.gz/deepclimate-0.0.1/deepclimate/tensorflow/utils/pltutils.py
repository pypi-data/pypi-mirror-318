

def plot_traincurve(df, ax, header, label=None, ylim=None):
    ax.set_facecolor('#F0F0F0')
    ax.plot(df['epoch'], df[f'{header}'], linewidth=4, color='blue', label='Training Set')
    ax.plot(df['epoch'], df[f'val_{header}'], linewidth=2, color='red', label='Validation Set')

    min_val_loss_idx = df[f'val_{header}'].idxmin()
    min_val_loss_epoch = df.at[min_val_loss_idx, 'epoch']
    min_val_loss_value = df.at[min_val_loss_idx, f'val_{header}']

    ax.text(0.3, 0.9, f"Min.val.loss epoch: {min_val_loss_epoch}", ha='left', va='top', fontweight='normal', transform=ax.transAxes, fontsize=14)
    ax.text(0.3, 0.96, f"Min.val.loss value: {min_val_loss_value.round(4)}", ha='left', va='top', fontweight='normal', transform=ax.transAxes, fontsize=14)
    
    # ax.scatter(min_val_loss_epoch, min_val_loss_value, color='green', s=1000, marker='*', zorder=5)
    ax.axvline(x=min_val_loss_epoch, color='green', linewidth=2, linestyle='--', alpha=0.6, label='Best Model')

    ax.tick_params(axis='both', labelsize=14)
    ax.set_xlabel('EPOCHS', fontsize=16)
    ax.set_ylabel(header.upper(), fontsize=16)

    if not ylim is None:
        ax.set_ylim(ylim[0], ylim[1])

    if label is not None:
        ax.set_title(label, fontsize=18, fontweight='bold')