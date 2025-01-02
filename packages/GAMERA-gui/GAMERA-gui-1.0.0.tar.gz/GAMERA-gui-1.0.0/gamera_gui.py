import sys
import os
import numpy as np
import h5py
import matplotlib.pyplot as plt
import warnings
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QComboBox,
    QSlider,
    QWidget,
    QMessageBox,
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPalette
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from astropy.time import Time
from matplotlib.animation import FuncAnimation


plt.rcParams.update({"font.size": 13})
warnings.filterwarnings("ignore")


# Class: extract_GAMERA_simulation
class extract_GAMERA_simulation:
    def __init__(self, filename):
        self.filename = filename
        self.h5_data = h5py.File(self.filename)
        self.keys = list(self.h5_data.keys())
        self.X = self.h5_data["X"][:]
        self.Y = self.h5_data["Y"][:]
        self.Z = self.h5_data["Z"][:]
        self.quantitites = list(self.h5_data["Step#0"].keys())

        self.r = np.sqrt(self.X**2 + self.Y**2 + self.Z**2)
        self.theta = np.rad2deg(np.arccos(self.Z / self.r))
        self.phi = np.rad2deg(np.arctan2(self.Y, self.X)) % 360
        self.radial_scaling = self.r / 21.5

        self.mjd_times = self.h5_data["timeAttributeCache"]["MJD"][:]
        self.ntime = len(self.mjd_times)

        if (
            "Br" not in self.quantitites
            or "Btheta" not in self.quantitites
            or "Bphi" not in self.quantitites
            or "Vr" not in self.quantitites
            or "Vtheta" not in self.quantitites
            or "Vphi" not in self.quantitites
        ):
            self.h5_data.close()
            with h5py.File(self.filename, "a") as hdf:
                for timeindex in range(self.ntime):
                    group = hdf["Step#" + str(timeindex)]
                    if (
                        "Br" not in self.quantitites
                        or "Btheta" not in self.quantitites
                        or "Bphi" not in self.quantitites
                    ):
                        bx = hdf["Step#" + str(timeindex)]["Bx"][:]
                        by = hdf["Step#" + str(timeindex)]["By"][:]
                        bz = hdf["Step#" + str(timeindex)]["Bz"][:]
                        shape = bx.shape
                        theta = np.deg2rad(self.theta)[
                            : shape[0], : shape[1], : shape[2]
                        ]
                        phi = np.deg2rad(self.phi)[: shape[0], : shape[1], : shape[2]]
                        br = (
                            bx * np.sin(theta) * np.cos(phi)
                            + by * np.sin(theta) * np.sin(phi)
                            + bz * np.cos(theta)
                        )
                        btheta = (
                            bx * np.cos(theta) * np.cos(phi)
                            + by * np.cos(theta) * np.sin(phi)
                            - bz * np.sin(theta)
                        )
                        bphi = -bx * np.sin(phi) + by * np.cos(phi)
                        group.create_dataset("Br", data=br)
                        group.create_dataset("Btheta", data=btheta)
                        group.create_dataset("Bphi", data=bphi)
                    if (
                        "Vr" not in self.quantitites
                        or "Vtheta" not in self.quantitites
                        or "Vphi" not in self.quantitites
                    ):
                        vx = hdf["Step#" + str(timeindex)]["Vx"][:]
                        vy = hdf["Step#" + str(timeindex)]["Vy"][:]
                        vz = hdf["Step#" + str(timeindex)]["Vz"][:]
                        shape = vx.shape
                        theta = np.deg2rad(self.theta)[
                            : shape[0], : shape[1], : shape[2]
                        ]
                        phi = np.deg2rad(self.phi)[: shape[0], : shape[1], : shape[2]]
                        vr = (
                            vx * np.sin(theta) * np.cos(phi)
                            + vy * np.sin(theta) * np.sin(phi)
                            + vz * np.cos(theta)
                        )
                        vtheta = (
                            vx * np.cos(theta) * np.cos(phi)
                            + vy * np.cos(theta) * np.sin(phi)
                            - vz * np.sin(theta)
                        )
                        vphi = -vx * np.sin(phi) + vy * np.cos(phi)
                        group.create_dataset("Vr", data=vr)
                        group.create_dataset("Vtheta", data=vtheta)
                        group.create_dataset("Vphi", data=vphi)
            self.h5_data = h5py.File(self.filename)
            self.quantitites = list(self.h5_data["Step#0"].keys())
        if "timeseries" not in self.keys:
            self.h5_data.close()
            rate = 0.9856
            with h5py.File(self.filename, "a") as hdf:
                group = hdf.create_group("timeseries")
                for quantity in self.quantitites:
                    y_value = []
                    for i in range(self.ntime):
                        time_diff = self.mjd_times[i] - self.mjd_times[0]
                        earth_X = 214 * np.cos(np.deg2rad(rate) * time_diff)
                        earth_Y = 214 * np.sin(np.deg2rad(rate) * time_diff)
                        data = hdf["Step#" + str(i)][quantity][:]
                        shape = data.shape
                        two_D_data = data[:, int(shape[1] / 2), :]
                        ec_r = self.r[0, int(shape[1] / 2), : shape[2]]
                        ec_phi = self.phi[: shape[0], int(shape[1] / 2), 0]
                        R, Phi = np.meshgrid(ec_r, ec_phi)
                        X = R * np.cos(np.deg2rad(Phi))
                        Y = R * np.sin(np.deg2rad(Phi))
                        distances = np.sqrt((X - earth_X) ** 2 + (Y - earth_Y) ** 2)
                        # Find the indices of the nearest point
                        nearest_idx = np.unravel_index(
                            np.argmin(distances), distances.shape
                        )
                        # Get the value of the nearest point in the data array
                        y_value.append(two_D_data[nearest_idx[0], nearest_idx[1]])
                    y_value = np.array(y_value)
                    group.create_dataset(quantity, data=y_value)
        self.h5_data = h5py.File(self.filename)
        self.quantitites = list(self.h5_data["Step#0"].keys())

    def get_plot_ranges(self, quantity=""):
        timestamp = self.mjd_times[int(self.ntime / 2)]
        self.access_fulldata(timestamp, quantity=quantity)
        self.vmin = np.nanmin(self.fulldata) * 0.2
        self.vmax = np.nanmax(self.fulldata) * 0.2
        if self.vmin < 0 and np.abs(self.vmin) != self.vmax:
            self.vmin = -self.vmax

    def access_fulldata(self, timestamp, quantity=""):
        """
        Access data from GAMERA simulation cube
        Parameters
        ----------
        timestamp : str
            Timestamp in MJD
        quantity : str
            Physical quantity to extract ('Bx', 'By', 'Bz', 'Cs', 'D', 'Jx', 'Jy', 'Jz', 'P', 'Pb', 'Vx', 'Vy', 'Vz')
        """
        timeindex = np.argmin(np.abs(timestamp - self.mjd_times))
        if quantity in [
            "Bx",
            "By",
            "Bz",
            "Cs",
            "D",
            "Jx",
            "Jy",
            "Jz",
            "P",
            "Pb",
            "Vx",
            "Vy",
            "Vz",
            "Br",
            "Btheta",
            "Bphi",
            "Vr",
            "Vtheta",
            "Vphi",
        ]:
            self.fulldata = self.h5_data["Step#" + str(timeindex)][quantity][:]
        else:
            print("Please provide a correct quantity")
            return
        shape = self.fulldata.shape
        if quantity not in ["Vx", "Vy", "Vz", "Vr", "Vphi", "Vtheta"]:
            self.fulldata = (
                self.fulldata
                * (self.radial_scaling[: shape[0], : shape[1], : shape[2]]) ** 2
            )

    def get_two_D_data(self, projection="ecliptic"):
        """
        Get 2D projected data on ecliptic or meridonial plane
        Parameters
        ----------
        projection : str
            Projection plane
        """
        shape = self.fulldata.shape
        if projection == "ecliptic":
            two_D_data = self.fulldata[:, int(shape[1] / 2), :]
            ec_r = self.r[0, int(shape[1] / 2), : shape[2]]
            ec_phi = self.phi[: shape[0], int(shape[1] / 2), 0]
            R, Phi = np.meshgrid(ec_r, ec_phi)
            two_D_X = R * np.cos(np.deg2rad(Phi))
            two_D_Y = R * np.sin(np.deg2rad(Phi))
            return two_D_X, two_D_Y, two_D_data
        else:
            shape = self.fulldata.shape
            phi = np.deg2rad(self.phi[: shape[0], : shape[1], : shape[2]]) % (2 * np.pi)
            X = self.X[: shape[0], : shape[1], : shape[2]]
            Z = self.Z[: shape[0], : shape[1], : shape[2]]
            data_cube = self.fulldata

            # Filter for the YZ-plane (phi ~ 90° or pi/2)
            phi_target = 0
            phi_tolerance = np.pi / 180  # 1 degree in radians
            mask = np.abs(phi - phi_target) < phi_tolerance

            # Apply the mask to extract Y, Z, and data values
            masked_X = np.ma.masked_array(X, mask=~mask)
            masked_Z = np.ma.masked_array(Z, mask=~mask)
            masked_data = np.ma.masked_array(data_cube, mask=~mask)

            # Reshape the masked arrays to 2D
            X_2D_0 = masked_X[mask].reshape(masked_X.shape[1], masked_X.shape[2])
            Z_2D_0 = masked_Z[mask].reshape(masked_Z.shape[1], masked_Z.shape[2])
            data_2D_0 = masked_data[mask].reshape(
                masked_data.shape[1], masked_data.shape[2]
            )

            # Filter for the YZ-plane (phi ~ 90° or pi/2)
            phi_target = np.pi
            phi_tolerance = np.pi / 180  # 1 degree in radians
            mask = np.abs(phi - phi_target) < phi_tolerance

            # Apply the mask to extract Y, Z, and data values
            masked_X = np.ma.masked_array(X, mask=~mask)
            masked_Z = np.ma.masked_array(Z, mask=~mask)
            masked_data = np.ma.masked_array(data_cube, mask=~mask)

            # Reshape the masked arrays to 2D
            X_2D_1 = masked_X[mask].reshape(masked_X.shape[1], masked_X.shape[2])
            Z_2D_1 = masked_Z[mask].reshape(masked_Z.shape[1], masked_Z.shape[2])
            data_2D_1 = masked_data[mask].reshape(
                masked_data.shape[1], masked_data.shape[2]
            )
            return X_2D_0, Z_2D_0, data_2D_0, X_2D_1, Z_2D_1, data_2D_1


# Class: HDF5Plotter
class HDF5Plotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("GAMERA Simulation Viewer")
        screen = QApplication.primaryScreen().availableGeometry()
        width, height = int(screen.width() * 0.8), int(screen.height() * 0.8)
        if width < height:
            height = width
        else:
            width = height
        self.setGeometry(
            (screen.width() - 2 * width) // 2,
            (screen.height() - 2 * height) // 2,
            int(1.5 * width),
            2 * height,
        )
        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Layouts
        self.main_layout = QVBoxLayout(self.central_widget)
        self.control_layout = QHBoxLayout()

        # File load button
        self.load_button = QPushButton("Load HDF5 File")
        self.load_button.clicked.connect(self.load_file)
        self.control_layout.addWidget(self.load_button)

        # Quantity selection dropdown
        self.quantity_dropdown = QComboBox()
        self.quantity_dropdown.currentIndexChanged.connect(self.update_quantity)
        self.control_layout.addWidget(QLabel("Quantity:"))
        self.control_layout.addWidget(self.quantity_dropdown)

        # Navigation buttons
        self.prev_button = QPushButton("<<")
        self.prev_button.clicked.connect(self.prev_frame)
        self.prev_button.setEnabled(False)
        self.control_layout.addWidget(self.prev_button)

        self.next_button = QPushButton(">>")
        self.next_button.clicked.connect(self.next_frame)
        self.next_button.setEnabled(False)
        self.control_layout.addWidget(self.next_button)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.toggle_play)
        self.play_button.setEnabled(False)
        self.control_layout.addWidget(self.play_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_play)
        self.stop_button.setEnabled(False)
        self.control_layout.addWidget(self.stop_button)

        self.main_layout.addLayout(self.control_layout)

        # Speed slider
        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(1000)
        self.speed_slider.setValue(1)
        self.speed_slider.setInvertedAppearance(True)
        self.speed_slider.setInvertedControls(True)

        # Save button
        self.save_button = QPushButton("Save Plot")
        self.save_button.clicked.connect(self.save_plot)
        self.control_layout.addWidget(self.save_button)

        # Save button
        self.save_button = QPushButton("Save Movie")
        self.save_button.clicked.connect(self.save_movie)
        self.control_layout.addWidget(self.save_button)

        # Customize slider to remove blue color
        palette = QPalette()
        palette.setColor(
            QPalette.Highlight, QColor(0, 0, 0, 0)
        )  # Transparent highlight
        self.speed_slider.setPalette(palette)

        self.main_layout.addWidget(QLabel("Playback Speed:"))
        self.main_layout.addWidget(self.speed_slider)

        # Matplotlib figure
        self.figure = plt.figure(figsize=(15, 20), constrained_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.ax0 = plt.subplot2grid((4, 4), (0, 0), colspan=2, rowspan=3)
        self.ax1 = plt.subplot2grid((4, 4), (0, 2), colspan=2, rowspan=3)
        self.ax2 = plt.subplot2grid((4, 4), (3, 0), colspan=4, rowspan=1)
        self.main_layout.addWidget(self.canvas)
        self.figure.patch.set_facecolor("white")
        self.ax0.set_facecolor("white")
        self.ax0.set_xticks([])
        self.ax0.set_yticks([])
        self.ax1.set_facecolor("white")
        self.ax1.set_xticks([])
        self.ax1.set_yticks([])
        self.ax2.set_facecolor("white")
        self.ax2.set_xticks([])
        self.ax2.set_yticks([])
        for spine in self.ax0.spines.values():
            spine.set_visible(False)
        for spine in self.ax1.spines.values():
            spine.set_visible(False)
        for spine in self.ax2.spines.values():
            spine.set_visible(False)

        # Timer for playback
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.play_continuous)

        # Data variables
        self.filepath = None
        self.file_label = QLabel("No file uploaded")
        self.main_layout.addWidget(self.file_label)
        self.hdf5 = None
        self.timestamps = []
        self.quantity = None
        self.current_frame = 0
        self.is_playing = False
        self.vline = None
        self.cbar = None

    def save_movie(self):
        # Open file dialog to select save location
        options = QFileDialog.Options()
        if self.filepath != None:
            path = os.path.dirname(self.filepath)
        else:
            path = ""
        filepath, _ = QFileDialog.getSaveFileName(
            self,
            "Save Movie",
            path,
            "MP4 Files (*.mp4);;GIF Files (*.gif);;All Files (*)",
            options=options,
        )
        if filepath:
            # Define animation function
            def update_frame(frame):
                self.current_frame = frame
                self.plot_frame()
                return (self.canvas,)

            # Create the animation
            ani = FuncAnimation(
                self.figure,
                update_frame,
                frames=len(self.timestamps),
                interval=self.speed_slider.value(),
                blit=False,  # Use `False` for complex plots
            )

            # Save the animation
            try:
                if filepath.endswith(".gif"):
                    ani.save(
                        filepath, writer="pillow", fps=10, dpi=self.canvas.figure.dpi
                    )
                else:
                    ani.save(
                        filepath, writer="ffmpeg", fps=10, dpi=self.canvas.figure.dpi
                    )
                # Show success popup
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Save Movie")
                msg.setText(f"Movie successfully saved to:\n{filepath}")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            except Exception as e:
                # Show error popup
                msg = QMessageBox(self)
                msg.setIcon(QMessageBox.Critical)
                msg.setWindowTitle("Error Saving Movie")
                msg.setText(f"Failed to save the movie:\n{str(e)}")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()

    def save_plot(self):
        # Open file dialog to select save location
        options = QFileDialog.Options()
        if self.filepath != None:
            path = os.path.dirname(self.filepath)
        else:
            path = ""
        filepath, _ = QFileDialog.getSaveFileName(
            self,
            "Save Plot",
            path,
            "PNG Files (*.png);;JPEG Files (*.jpg);;PDF Files (*.pdf);;All Files (*)",
            options=options,
        )
        if filepath:
            # Save the figure
            self.canvas.figure.savefig(
                filepath, dpi=self.canvas.figure.dpi, bbox_inches=None
            )
            print(f"Plot saved to {filepath}")
            # Show confirmation popup
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Save Plot")
            msg.setText(f"Plot successfully saved to:\n{filepath}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setGeometry(
                self.geometry().center().x() - 150,  # Adjust width offset
                self.geometry().center().y() - 75,  # Adjust height offset
                300,  # Width of the popup
                150,  # Height of the popup
            )
            msg.exec_()

    def load_file(self):
        options = QFileDialog.Options()
        self.filepath, _ = QFileDialog.getOpenFileName(
            self, "Select HDF5 File", "", "HDF5 Files (*.h5)", options=options
        )
        self.file_label.setText("No file uploaded")
        if self.filepath:
            self.file_label.setText("Loading file...")
            QApplication.processEvents()
            self.hdf5 = extract_GAMERA_simulation(self.filepath)
            self.file_label.setText(f"Loaded File: {os.path.basename(self.filepath)}")
            self.timestamps = self.hdf5.mjd_times[1:]
            self.quantity_dropdown.addItems(self.hdf5.quantitites)
            self.quantity = self.hdf5.quantitites[0]
            self.hdf5.get_plot_ranges(self.quantity)
            self.prev_button.setEnabled(True)
            self.next_button.setEnabled(True)
            self.play_button.setEnabled(True)
            self.stop_button.setEnabled(True)
            for spine in self.ax0.spines.values():
                spine.set_visible(True)
            for spine in self.ax1.spines.values():
                spine.set_visible(True)
            for spine in self.ax2.spines.values():
                spine.set_visible(True)
            self.plot_frame()

    def update_quantity(self):
        self.quantity = self.quantity_dropdown.currentText()
        self.hdf5.get_plot_ranges(self.quantity)
        self.current_frame = 0
        self.vmin = self.hdf5.vmin
        self.vmax = self.hdf5.vmax
        self.plot_timeseries(self.quantity)
        self.plot_frame()

    def plot_timeseries(self, quantity):
        y_value = self.hdf5.h5_data["timeseries"][quantity][1:]
        self.ax2.clear()
        self.ax2.plot(self.timestamps - self.timestamps[0], y_value)
        if len(quantity) > 1:
            if len(quantity[1:]) > 1:
                self.ax2.set_ylabel(rf"${quantity[0]}_{{\{quantity[1:]}}}$")
            else:
                self.ax2.set_ylabel(rf"${quantity[0]}_{{{quantity[1:]}}}$")
        else:
            self.ax2.set_ylabel(quantity)
        self.ax2.set_xlabel("Days")
        self.vline = self.ax2.axvline(
            self.timestamps[0] - self.timestamps[0], color="red"
        )
        self.canvas.draw()

    def plot_frame(self):
        self.hdf5.access_fulldata(self.timestamps[self.current_frame], self.quantity)
        if self.quantity == "D":
            cmap = "copper_r"
            cmap_title = r"$n (\frac{r_0}{r})^2\ \mathrm{cm}^{-3}$"
        elif self.quantity == "Bx":
            cmap = "bwr"
            cmap_title = r"$B_X (\frac{r_0}{r})^2\ \mathrm{nT}$"
        elif self.quantity == "By":
            cmap = "bwr"
            cmap_title = r"$B_Y (\frac{r_0}{r})^2\ \mathrm{nT}$"
        elif self.quantity == "Bz":
            cmap = "bwr"
            cmap_title = r"$B_Z (\frac{r_0}{r})^2\ \mathrm{nT}$"
        elif self.quantity == "Br":
            cmap = "bwr"
            cmap_title = r"$B_r (\frac{r_0}{r})^2\ \mathrm{nT}$"
        elif self.quantity == "Btheta":
            cmap = "bwr"
            cmap_title = r"$B_\theta (\frac{r_0}{r})^2\ \mathrm{nT}$"
        elif self.quantity == "Bphi":
            cmap = "bwr"
            cmap_title = r"$B_\phi (\frac{r_0}{r})^2\ \mathrm{nT}$"
        elif self.quantity == "Vx":
            cmap = "plasma_r"
            cmap_title = r"$V_X\ \mathrm{km/s}$"
        elif self.quantity == "Vy":
            cmap = "plasma_r"
            cmap_title = r"$V_Y\ \mathrm{km/s}$"
        elif self.quantity == "Vz":
            cmap = "plasma_r"
            cmap_title = r"$V_Z\ \mathrm{km/s}$"
        elif self.quantity == "Vr":
            cmap = "plasma_r"
            cmap_title = r"$V_r\ \mathrm{km/s}$"
        elif self.quantity == "Vtheta":
            cmap = "plasma_r"
            cmap_title = r"$V_\theta\ \mathrm{km/s}$"
        elif self.quantity == "Vphi":
            cmap = "plasma_r"
            cmap_title = r"$V_\phi\ \mathrm{km/s}$"
        else:
            cmap = "cividis"
            cmap_title = self.quantity + r"$(\frac{r_0}{r})^2$"
        timestamp = self.timestamps[self.current_frame]
        self.ax0.clear()
        self.ax1.clear()
        two_D_X, two_D_Y, two_D_data = self.hdf5.get_two_D_data(projection="ecliptic")
        mesh0 = self.ax0.pcolormesh(
            two_D_X,
            two_D_Y,
            two_D_data,
            shading="nearest",
            cmap=cmap,
            vmin=self.vmin,
            vmax=self.vmax,
        )
        self.ax0.set_xlabel(r"X ($R_\odot$)")
        self.ax0.set_ylabel(r"Y ($R_\odot$)")
        two_D_X0, two_D_Z0, two_D_data0, two_D_X1, two_D_Z1, two_D_data1 = (
            self.hdf5.get_two_D_data(projection="meridonidal")
        )
        self.ax1.pcolormesh(
            two_D_X0,
            two_D_Z0,
            two_D_data0,
            shading="nearest",
            cmap=cmap,
            vmin=self.vmin,
            vmax=self.vmax,
        )
        mesh1 = self.ax1.pcolormesh(
            two_D_X1,
            two_D_Z1,
            two_D_data1,
            shading="nearest",
            cmap=cmap,
            vmin=self.vmin,
            vmax=self.vmax,
        )
        self.ax1.set_xlabel(r"X ($R_\odot$)")
        self.ax1.set_ylabel(r"Z ($R_\odot$)")
        if self.cbar != None:
            try:
                self.cbar.remove()
            except:
                pass
        self.cbar = self.figure.colorbar(
            mesh1,
            ax=[self.ax0, self.ax1],
            orientation="vertical",
            pad=0.01,
            shrink=0.8,
            aspect=30,
        )
        theta = np.linspace(0, 2 * np.pi, 1000)
        self.ax0.plot(21.5 * np.cos(theta), 21.5 * np.sin(theta), color="k")
        self.ax1.plot(21.5 * np.cos(theta), 21.5 * np.sin(theta), color="k")

        time_mjd = Time(timestamp, format="mjd")
        isot = time_mjd.isot
        self.figure.suptitle(
            cmap_title
            + ", Time: "
            + str(isot.split("T")[0])
            + " "
            + str(isot.split("T")[1].split(".")[0]),
            y=0.98,
        )
        rate = 0.9856
        time_diff = self.timestamps[self.current_frame] - self.hdf5.mjd_times[0]
        if self.vline != None:
            self.vline.remove()
        self.vline = self.ax2.axvline(
            self.timestamps[self.current_frame] - self.timestamps[0], color="red"
        )
        earth_X = 214 * np.cos(np.deg2rad(rate) * time_diff)
        earth_Y = 214 * np.sin(np.deg2rad(rate) * time_diff)
        self.ax0.scatter(
            earth_X, earth_Y, color="green", marker="o", s=80, label="Earth"
        )
        self.ax1.scatter(earth_X, 0, color="green", marker="o", s=80, label="Earth")
        self.ax0.legend(loc="upper right")
        self.ax1.legend(loc="upper right")
        self.ax0.set_xlim(-230, 230)
        self.ax0.set_ylim(-230, 230)
        self.ax0.set_aspect("equal")
        self.ax1.set_xlim(-230, 230)
        self.ax1.set_ylim(-230, 230)
        self.ax1.set_aspect("equal")
        self.canvas.draw()

    def prev_frame(self):
        if self.current_frame > 0:
            self.current_frame -= 1
            self.plot_frame()

    def next_frame(self):
        if self.current_frame < len(self.timestamps) - 1:
            self.current_frame += 1
            self.plot_frame()

    def toggle_play(self):
        self.is_playing = not self.is_playing
        if self.is_playing:
            self.timer.start(self.speed_slider.value())

    def stop_play(self):
        self.is_playing = False
        self.timer.stop()

    def play_continuous(self):
        if self.is_playing and self.current_frame < len(self.timestamps) - 1:
            self.next_frame()
        else:
            self.current_frame = 0
            self.plot_frame()
        if self.is_playing:
            self.timer.start(self.speed_slider.value())


def main():
    app = QApplication(["gamera-gui"])
    app.setStyleSheet("QWidget { font-size: 16px; }")
    window = HDF5Plotter()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
