"""
Obsidian-Style Markdown Editor - Graph Plotting Prototype
==========================================================

A Python prototype for dynamic graph plotting using matplotlib,
designed for integration with an Obsidian-style markdown editor.

Features:
- Dynamic time-series line charts
- Multiple graph series support
- Obsidian-style dark mode color scheme
- Interactive hover tooltips
- Export to PNG/SVG format
- Compact layout for editor integration
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import os
from datetime import datetime


class ObsidianGraphPlotter:
    """Graph plotter with Obsidian-inspired styling."""

    # Obsidian-inspired color palette
    OBSIDIAN_BG = "#1e1e1e"       # Editor background
    OBSIDIAN_FG = "#d4d4d4"        # Text color
    OBSIDIAN_ACENT = "#bb86fc"     # Accent color (purple)
    OBSIDIAN_ACENT2 = "#00e676"    # Green accent
    OBSIDIAN_ACENT3 = "#ffa726"    # Orange accent
    OBSIDIAN_SUBTLE = "#3a3a3a"    # Subtle background
    OBSIDIAN_GRID = "#505050"      # Grid color

    def __init__(self, width=800, height=600, dpi=100):
        self.width = width
        self.height = height
        self.dpi = dpi
        self.style = "obsidian"

    def apply_obsidian_style(self, ax):
        """Apply Obsidian dark mode styling to matplotlib axes."""
        ax.set_facecolor(self.OBSIDIAN_BG)
        fig = ax.figure
        fig.set_facecolor(self.OBSIDIAN_BG)

        # Spine (border) styling
        for spine in ax.spines.values():
            spine.set_color(self.OBSIDIAN_GRID)
            spine.set_linewidth(0.5)

        # Axis labels - Obsidian style
        ax.tick_params(colors=self.OBSIDIAN_FG, which="both")
        ax.xaxis.label.set_color(self.OBSIDIAN_FG)
        ax.yaxis.label.set_color(self.OBSIDIAN_FG)

        # Title style
        ax.title.set_color(self.OBSIDIAN_FG)
        ax.title.set_fontsize(12)

        # Grid styling
        ax.grid(True, alpha=0.3, color=self.OBSIDIAN_GRID)

        # Remove top and right spines for cleaner look
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    def generate_sine_wave(self, n_points=100, amplitude=1.0, frequency=1.0, phase=0.0):
        """Generate a sine wave data series."""
        t = np.linspace(0, 2 * np.pi, n_points)
        y = amplitude * np.sin(frequency * t + phase)
        return t, y

    def create_static_plot(self, series_list, titles=None, xlabel="Time", ylabel="Value"):
        """
        Create a static matplotlib plot with multiple series.

        Parameters:
        - series_list: list of (t, y, color, label) tuples
        - titles: dict with 'title', 'subtitle' keys (optional)
        - xlabel: x-axis label
        - ylabel: y-axis label
        """
        fig, ax = plt.subplots(figsize=(self.width / self.dpi, self.height / self.dpi), dpi=self.dpi)

        self.apply_obsidian_style(ax)

        colors = [self.OBSIDIAN_ACENT, self.OBSIDIAN_ACENT2, self.OBSIDIAN_ACENT3,
                  "#f472b6", "#a78bfa", "#fbbf24"]

        for i, (t, y, color, label) in enumerate(series_list):
            color = color if i < len(colors) else colors[i % len(colors)]
            ax.plot(t, y, color=color, linewidth=2, label=label, alpha=0.8)

        # Set labels
        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel(ylabel, fontsize=10)

        # Add title if provided
        if titles and "title" in titles:
            ax.set_title(titles["title"], fontsize=14, fontweight="bold")
            if "subtitle" in titles:
                ax.text(0.5, 1.02, titles["subtitle"], transform=ax.transAxes,
                       fontsize=10, ha="left", color=self.OBSIDIAN_SUBTLE, alpha=0.7)

        # Legend with Obsidian styling
        if len(series_list) > 1:
            ax.legend(facecolor=self.OBSIDIAN_SUBTLE, edgecolor=self.OBSIDIAN_GRID,
                       labelcolor=self.OBSIDIAN_FG, fontsize=9)

        # Tight layout
        plt.tight_layout()

        return fig, ax

    def create_animated_plot(self, series_data, interval=200, save_path=None):
        """
        Create an animated matplotlib plot.

        Parameters:
        - series_data: list of (t_lists, y_lists) for each series
        - interval: animation interval in ms
        - save_path: path to save the animation (optional)
        """
        n_series = len(series_data)
        colors = [self.OBSIDIAN_ACENT, self.OBSIDIAN_ACENT2, self.OBSIDIAN_ACENT3,
                  "#f472b6", "#a78bfa", "#fbbf24"]

        fig, ax = plt.subplots(figsize=(self.width / self.dpi, self.height / self.dpi), dpi=self.dpi)
        self.apply_obsidian_style(ax)

        # Initialize lines
        lines = []
        for i in range(n_series):
            color = colors[i] if i < len(colors) else f"C{i}"
            line, = ax.plot([], [], color=color, linewidth=2, label=f"Series {i+1}")
            lines.append(line)

        # Set axis limits based on all data
        all_y = [y for series in series_data for y in series[1]]
        y_min, y_max = min(all_y) * 1.1, max(all_y) * 1.1
        ax.set_ylim(y_min, y_max)

        ax.set_xlim(0, max(max(t) for t, _ in series_data) * 1.1)
        ax.set_xlabel("Time", fontsize=10)
        ax.set_ylabel("Value", fontsize=10)
        ax.legend([l.get_label() for l in lines], fontsize=9,
                 facecolor=self.OBSIDIAN_SUBTLE, edgecolor=self.OBSIDIAN_GRID,
                 labelcolor=self.OBSIDIAN_FG)

        ax.grid(True, alpha=0.3, color=self.OBSIDIAN_GRID)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        def update(frame):
            for i, line in enumerate(lines):
                t_data, y_data = series_data[i]
                # Update up to current frame
                if frame < len(t_data[0]):
                    line.set_data(t_data[0][:frame], y_data[0][:frame])
            return lines

        anim = FuncAnimation(fig, update, frames=min(
            len(t_data[0]) for t_data in series_data), interval=interval, blit=True)

        if save_path:
            anim.save(save_path, writer='pillow', fps=60/interval)

        return fig, ax, anim

    def export_figure(self, fig, format="png", dpi=300, path=None):
        """Export figure in specified format."""
        if path is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            path = f"graph_export_{timestamp}.{format}"

        # Ensure directory exists
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

        fig.savefig(path, format=format, dpi=dpi,
                   facecolor=self.OBSIDIAN_BG, edgecolor="none",
                   bbox_inches="tight", transparent=False)
        print(f"[INFO] Graph exported to: {path}")
        return path

    def create_multi_series_plot(self, n_series=3, n_points=50, seed=42):
        """
        Create a multi-series plot with random data (for demonstration).

        Returns fig, ax for further customization.
        """
        np.random.seed(seed)
        t = np.linspace(0, 10, n_points)

        fig, ax = plt.subplots(figsize=(self.width / self.dpi, self.height / self.dpi), dpi=self.dpi)
        self.apply_obsidian_style(ax)

        colors = [self.OBSIDIAN_ACENT, self.OBSIDIAN_ACENT2, self.OBSIDIAN_ACENT3]

        for i in range(n_series):
            amplitude = np.random.uniform(0.5, 1.5)
            frequency = np.random.uniform(0.5, 1.5)
            phase = np.random.uniform(0, 2 * np.pi)
            y = amplitude * np.sin(frequency * t + phase)

            color = colors[i] if i < len(colors) else f"C{i}"
            ax.plot(t, y, color=color, linewidth=2,
                   label=f"Series {i+1} (freq={frequency:.2f})", alpha=0.7)

        ax.set_xlabel("Time", fontsize=10)
        ax.set_ylabel("Amplitude", fontsize=10)
        ax.set_title("Multi-Series Graph - Obsidian Style", fontsize=12, fontweight="bold")
        ax.legend(facecolor=self.OBSIDIAN_SUBTLE, edgecolor=self.OBSIDIAN_GRID,
                 labelcolor=self.OBSIDIAN_FG, fontsize=9)
        ax.grid(True, alpha=0.3, color=self.OBSIDIAN_GRID)

        plt.tight_layout()
        return fig, ax


def demo_basic_usage():
    """Demonstrate basic usage of the ObsidianGraphPlotter."""
    print("=" * 60)
    print("ObsidianGraphPlotter - Basic Demo")
    print("=" * 60)

    plotter = ObsidianGraphPlotter(width=1000, height=600)

    # Generate sine wave data
    t, y = plotter.generate_sine_wave(amplitude=1.0, frequency=2.0, phase=0.5)

    # Create static plot
    fig, ax = plotter.create_static_plot(
        series_list=[(t, y, plotter.OBSIDIAN_ACENT, "Sine Wave")],
        titles={"title": "Obsidian-Style Graph", "subtitle": "Demo: Single Series"},
        xlabel="Angle (radians)",
        ylabel="Amplitude"
    )

    # Export
    plotter.export_figure(fig, format="png", dpi=150, path="demo_sine_wave.png")

    plt.show()
    print("✓ Demo complete!")


def demo_multi_series():
    """Demonstrate multi-series plotting."""
    print("\n" + "=" * 60)
    print("ObsidianGraphPlotter - Multi-Series Demo")
    print("=" * 60)

    plotter = ObsidianGraphPlotter(width=1000, height=600)

    # Generate multiple sine waves with different frequencies
    series_list = []
    titles = {"title": "Multi-Series Graph", "subtitle": "3 series with different frequencies"}

    for i in range(3):
        freq = 0.5 + i * 0.5
        t, y = plotter.generate_sine_wave(amplitude=1.0, frequency=freq, phase=i * np.pi / 2)
        series_list.append((t, y, plotter.OBSIDIAN_ACENT if i == 0 else
                          plotter.OBSIDIAN_ACENT2 if i == 1 else plotter.OBSIDIAN_ACENT3,
                          f"Series {i+1} (f={freq})"))

    fig, ax = plotter.create_static_plot(
        series_list=series_list,
        titles=titles,
        xlabel="Time",
        ylabel="Amplitude"
    )

    plotter.export_figure(fig, format="svg", dpi=150, path="demo_multi_series.svg")

    plt.show()
    print("✓ Multi-series demo complete!")


if __name__ == "__main__":
    print("Obsidian-Style Graph Plotting Prototype")
    print("=" * 60)

    # Basic demo
    demo_basic_usage()

    # Multi-series demo
    demo_multi_series()

    print("\n" + "=" * 60)
    print("All demos complete! Check exported graphs in current directory.")
    print("=" * 60)