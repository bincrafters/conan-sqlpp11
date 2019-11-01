from conans import ConanFile, CMake, tools, RunEnvironment
import os


class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        for example in ['insert', 'update', 'select', 'remove']:
            bin_path = os.path.join("bin", "sqlpp11_examples %s" % example)
            self.run(bin_path, run_environment=True)
