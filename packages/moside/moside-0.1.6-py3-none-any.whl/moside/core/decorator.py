from PySide6.QtWidgets import QMainWindow, QDialog, QWidget


def modern(cls):
    # 判断cls类型，装载不同的基类
    if issubclass(cls, QMainWindow):
        from ..components.modern_window import ModernMainWindow

        class ModernWindow(cls, ModernMainWindow):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.apply_modern()  # 应用现代UI
                if hasattr(self, 'after_modern'):
                    self.after_modern()  # 应用现代UI后的操作

    elif issubclass(cls, QDialog):
        from ..components.modern_window import ModernDialog

        class ModernWindow(cls, ModernDialog):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.apply_modern()  # 应用现代UI
                if hasattr(self, 'after_modern'):
                    self.after_modern()  # 应用现代UI后的操作

    elif issubclass(cls, QWidget):
        from ..components.modern_window import ModernWidget

        class ModernWindow(cls, ModernWidget):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.apply_modern()  # 应用现代UI
                if hasattr(self, 'after_modern'):
                    self.after_modern()  # 应用现代UI后的操作

    else:
        raise TypeError(f"Unsupported class type: {cls}")

    # 复制元信息
    ModernWindow.__name__ = cls.__name__
    ModernWindow.__module__ = cls.__module__
    ModernWindow.__doc__ = cls.__doc__

    return ModernWindow
