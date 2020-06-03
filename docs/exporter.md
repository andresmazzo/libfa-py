## Exporter

### Drivers
#### CSV V1
You have been playing with the lib, but now want to export some data to csv. Why? Once again, because it's cool to be able to migrate data between platforms. 

### Examples

```python
import libfa.exporter as faexporter
import libfa.exporter.csv_v1.lists as mlists
import libfa.exporter.csv_v1.ratings as mratings

faexporter.csv_v1.outputs()
['lists', 'ratings']

mlists.lists(data, '/your/path/file.csv')
mratings.ratings(data, '/your/path/file.csv')

```