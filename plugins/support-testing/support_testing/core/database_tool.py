'''
Created on April 3, 2014

@package: testing_support - database tool for test fixture
@copyright: 2014 Sourcefabric o.p.s.
@license: http://www.gnu.org/licenses/gpl-3.0.txt
@author: Ioan v. Pocol

Database tool for test fixture.
'''
import logging

# --------------------------------------------------------------------
log = logging.getLogger(__name__)

# --------------------------------------------------------------------

class DatabaseTool:
    
    def runscript(self, session, filename):
        try:
            f= open(filename , "r")
            session.execute('SET foreign_key_checks = 0')
            for sql in f:
                if sql == '\n' or sql[0] == '/' or sql[0] == '-':
                    pass
                else:
                    session.execute(str(sql))
            session.execute('SET foreign_key_checks = 1')
            session.commit()
        except Exception as e:
            log.error(e)
            session.rollback()
            return False
        finally:
            f.close()
        
        return True    