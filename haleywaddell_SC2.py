Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
from mininet.topo import Topo
 
class Topology0(Topo):
       def __init__(self):
             Topo.__init__(self)
             Ht1 = self.addHost('H1',ip = '10.0.1.10/24')
             Ht2 = self.addHost('H2', ip = '10.0.1.11/24')
             Ht3 = self.addHost('H3',ip='10.0.1.12/24')
             Ht4 = self.addHost('H4',ip='10.0.1.13/24')
             Ht5 = self.addHost('H5',ip='10.0.2.10/24')
             Ht6 = self.addHost('H6',ip='10.0.2.11/24')
             Ht7 = self.addHost('H7',ip='10.0.2.12/24')
             Ht8 = self.addHost('H8',ip='10.0.2.13/24')
             Ht9 = self.addHost('H9',ip='10.0.1.1/24')
             Ht10 = self.addHost('H10',ip='10.0.2.1/24')
             s9 = self.addSwitch('S9')
             s10 = self.addSwitch('S10')
              s11 = self.addSwitch('S11')
             s12 = self.addSwitch('S12')
             s13 = self.addSwitch('S13')
             s14 = self.addSwitch('S14')
             s15 = self.addSwitch('S15')
 
             self.addLink(s9,Ht9)
             self.addLink(s9,Ht10)
             self.addLink(s9,s10)
             self.addLink(s9,s13)
             self.addLink(s10,s11)
             self.addLink(s10,s12,bw=15,delay='10ms')
             self.addLink(s13,s14)
             self.addLink(s13,s15)
             self.addLink(s11,Ht1)
             self.addLink(s11,Ht2)
             self.addLink(s12,Ht3)
             self.addLink(s12,Ht4)
             self.addLink(s14,Ht5)
             self.addLink(s14,Ht6)
             self.addLink(s15,Ht7)
             self.addLink(s15,Ht8)
 
topos = { 'topology' :( lambda : Topology0() ) }