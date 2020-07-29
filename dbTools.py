import MySQLdb


class DBTool(object) :
    '''
    支持插入、更新、删除、查询(获取所有）操作
    在不需要的时候需要手动释放db资源
    '''

    def __init__(self, host=None, username=None, password=None, dbname=None) :
        if host is None and username is None and password is None and dbname is None :
            self.host = "localhost"
            self.username = "root"
            self.password = "123456"
            self.dbname = "apwd_center"
        else :
            self.host = host
            self.username = username
            self.password = password
            self.dbname = dbname
        self.max_connect_cnt = 20
        self.__conndb()
        self.Error = False

    # 连接数据库
    def __conndb(self) :
        connect_cnt = 0
        while True :
            try :
                self.db = MySQLdb.connect(self.host, self.username, self.password, self.dbname, charset='utf8')
            except Exception as e :
                # 当连接过多的时候或者其他异常的时候则sleep 1秒则重新连接
                # time.sleep(1) #这个可以注释掉
                connect_cnt += 1
                if connect_cnt < self.max_connect_cnt :
                    pass
                else :
                    raise e
            else :
                break
        self.cursor = self.db.cursor()

    # 装饰器函数保证更新数据的时候，连接OK，如果连接不正确重新连接
    def reconnectdb(func) :
        def wrapfunc(self, sql='') :
            try :
                self.db.ping()
            except :
                self.__conndb()
            self.Error = False
            return func(self, sql)

        return wrapfunc

    # 插入数据
    @reconnectdb
    def insertdb(self, sql) :
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as  e :
            # Rollback in case there is any error
            print("Error: unable to insertdb!")
            self.db.rollback()
            self.Error = True
            raise e

    # 更新数据
    @reconnectdb
    def updatedb(self, sql) :
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            # Rollback in case there is any error
            print("Error: unable to updatedb!")
            self.db.rollback()
            self.Error = True
            raise e

    # 获取数据
    @reconnectdb
    def fechdb(self, sql) :
        try :
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e :
            print("Error: unable to fecth data")
            self.Error = True
            raise e

    # 删除数据
    @reconnectdb
    def deldb(self, sql) :
        try :
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            # Rollback in case there is any error
            print("Error: unable to deldb!")
            self.db.rollback()
            self.Error = True
            raise e

    # 关闭数据
    def closedb(self) :
        try :
            self.db.close()
        except :
            print("数据库已关闭，无需关闭")


if __name__ == '__main__' :
    db = DBTool(host='localhost', username='root', password='123456', dbname='usercheck')
    db.insertdb("INSERT INTO fb(fid, fname, status)VALUES(%s,%s,%s);" % (1, 2, 3))
    # db.updatedb("UPDATE fb SET fname = 'hehe' WHERE fid = '1'")
    # db.insertdb("insert into User(Name) "
    #             "select "张三"\
    #             "where not exists(select UserId from User where Name="张三")")
