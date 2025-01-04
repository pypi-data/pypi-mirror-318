#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* bvbasic.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcbv.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsettype_ BVSETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsettype_ bvsettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgettype_ BVGETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgettype_ bvgettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetsizes_ BVSETSIZES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetsizes_ bvsetsizes
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetsizesfromvec_ BVSETSIZESFROMVEC
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetsizesfromvec_ bvsetsizesfromvec
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetsizes_ BVGETSIZES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetsizes_ bvgetsizes
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetnumconstraints_ BVSETNUMCONSTRAINTS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetnumconstraints_ bvsetnumconstraints
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetnumconstraints_ BVGETNUMCONSTRAINTS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetnumconstraints_ bvgetnumconstraints
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvresize_ BVRESIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvresize_ bvresize
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetactivecolumns_ BVSETACTIVECOLUMNS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetactivecolumns_ bvsetactivecolumns
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetactivecolumns_ BVGETACTIVECOLUMNS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetactivecolumns_ bvgetactivecolumns
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetmatrix_ BVSETMATRIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetmatrix_ bvsetmatrix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetmatrix_ BVGETMATRIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetmatrix_ bvgetmatrix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvapplymatrix_ BVAPPLYMATRIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvapplymatrix_ bvapplymatrix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvapplymatrixbv_ BVAPPLYMATRIXBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvapplymatrixbv_ bvapplymatrixbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetsignature_ BVSETSIGNATURE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetsignature_ bvsetsignature
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetsignature_ BVGETSIGNATURE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetsignature_ bvgetsignature
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetbuffervec_ BVSETBUFFERVEC
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetbuffervec_ bvsetbuffervec
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetbuffervec_ BVGETBUFFERVEC
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetbuffervec_ bvgetbuffervec
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetrandomcontext_ BVSETRANDOMCONTEXT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetrandomcontext_ bvsetrandomcontext
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetrandomcontext_ BVGETRANDOMCONTEXT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetrandomcontext_ bvgetrandomcontext
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetfromoptions_ BVSETFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetfromoptions_ bvsetfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetorthogonalization_ BVSETORTHOGONALIZATION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetorthogonalization_ bvsetorthogonalization
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetorthogonalization_ BVGETORTHOGONALIZATION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetorthogonalization_ bvgetorthogonalization
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetmatmultmethod_ BVSETMATMULTMETHOD
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetmatmultmethod_ bvsetmatmultmethod
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetmatmultmethod_ BVGETMATMULTMETHOD
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetmatmultmethod_ bvgetmatmultmethod
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetcolumn_ BVGETCOLUMN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetcolumn_ bvgetcolumn
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvrestorecolumn_ BVRESTORECOLUMN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvrestorecolumn_ bvrestorecolumn
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvcreatevec_ BVCREATEVEC
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvcreatevec_ bvcreatevec
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvcreatevecempty_ BVCREATEVECEMPTY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvcreatevecempty_ bvcreatevecempty
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetvectype_ BVSETVECTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetvectype_ bvsetvectype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetvectype_ BVGETVECTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetvectype_ bvgetvectype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvcreatemat_ BVCREATEMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvcreatemat_ bvcreatemat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetmat_ BVGETMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetmat_ bvgetmat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvrestoremat_ BVRESTOREMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvrestoremat_ bvrestoremat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvduplicate_ BVDUPLICATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvduplicate_ bvduplicate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvduplicateresize_ BVDUPLICATERESIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvduplicateresize_ bvduplicateresize
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetcachedbv_ BVGETCACHEDBV
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetcachedbv_ bvgetcachedbv
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvcopy_ BVCOPY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvcopy_ bvcopy
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvcopyvec_ BVCOPYVEC
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvcopyvec_ bvcopyvec
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvcopycolumn_ BVCOPYCOLUMN
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvcopycolumn_ bvcopycolumn
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetsplit_ BVGETSPLIT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetsplit_ bvgetsplit
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvrestoresplit_ BVRESTORESPLIT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvrestoresplit_ bvrestoresplit
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetsplitrows_ BVGETSPLITROWS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetsplitrows_ bvgetsplitrows
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvrestoresplitrows_ BVRESTORESPLITROWS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvrestoresplitrows_ bvrestoresplitrows
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetdefinitetolerance_ BVSETDEFINITETOLERANCE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetdefinitetolerance_ bvsetdefinitetolerance
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetdefinitetolerance_ BVGETDEFINITETOLERANCE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetdefinitetolerance_ bvgetdefinitetolerance
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvsetleadingdimension_ BVSETLEADINGDIMENSION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvsetleadingdimension_ bvsetleadingdimension
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define bvgetleadingdimension_ BVGETLEADINGDIMENSION
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define bvgetleadingdimension_ bvgetleadingdimension
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  bvsettype_(BV bv,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(bv);
/* insert Fortran-to-C conversion for type */
  FIXCHAR(type,cl0,_cltmp0);
*ierr = BVSetType(
	(BV)PetscToPointer((bv) ),_cltmp0);
  FREECHAR(type,_cltmp0);
}
SLEPC_EXTERN void  bvgettype_(BV bv,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(bv);
*ierr = BVGetType(
	(BV)PetscToPointer((bv) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for type */
*ierr = PetscStrncpy(type, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, type, cl0);
}
SLEPC_EXTERN void  bvsetsizes_(BV bv,PetscInt *n,PetscInt *N,PetscInt *m, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
*ierr = BVSetSizes(
	(BV)PetscToPointer((bv) ),*n,*N,*m);
}
SLEPC_EXTERN void  bvsetsizesfromvec_(BV bv,Vec t,PetscInt *m, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(t);
*ierr = BVSetSizesFromVec(
	(BV)PetscToPointer((bv) ),
	(Vec)PetscToPointer((t) ),*m);
}
SLEPC_EXTERN void  bvgetsizes_(BV bv,PetscInt *n,PetscInt *N,PetscInt *m, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLINTEGER(n);
CHKFORTRANNULLINTEGER(N);
CHKFORTRANNULLINTEGER(m);
*ierr = BVGetSizes(
	(BV)PetscToPointer((bv) ),n,N,m);
}
SLEPC_EXTERN void  bvsetnumconstraints_(BV V,PetscInt *nc, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
*ierr = BVSetNumConstraints(
	(BV)PetscToPointer((V) ),*nc);
}
SLEPC_EXTERN void  bvgetnumconstraints_(BV bv,PetscInt *nc, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLINTEGER(nc);
*ierr = BVGetNumConstraints(
	(BV)PetscToPointer((bv) ),nc);
}
SLEPC_EXTERN void  bvresize_(BV bv,PetscInt *m,PetscBool *copy, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
*ierr = BVResize(
	(BV)PetscToPointer((bv) ),*m,*copy);
}
SLEPC_EXTERN void  bvsetactivecolumns_(BV bv,PetscInt *l,PetscInt *k, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
*ierr = BVSetActiveColumns(
	(BV)PetscToPointer((bv) ),*l,*k);
}
SLEPC_EXTERN void  bvgetactivecolumns_(BV bv,PetscInt *l,PetscInt *k, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLINTEGER(l);
CHKFORTRANNULLINTEGER(k);
*ierr = BVGetActiveColumns(
	(BV)PetscToPointer((bv) ),l,k);
}
SLEPC_EXTERN void  bvsetmatrix_(BV bv,Mat B,PetscBool *indef, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(B);
*ierr = BVSetMatrix(
	(BV)PetscToPointer((bv) ),
	(Mat)PetscToPointer((B) ),*indef);
}
SLEPC_EXTERN void  bvgetmatrix_(BV bv,Mat *B,PetscBool *indef, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool B_null = !*(void**) B ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(B);
*ierr = BVGetMatrix(
	(BV)PetscToPointer((bv) ),B,indef);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! B_null && !*(void**) B) * (void **) B = (void *)-2;
}
SLEPC_EXTERN void  bvapplymatrix_(BV bv,Vec x,Vec y, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(x);
CHKFORTRANNULLOBJECT(y);
*ierr = BVApplyMatrix(
	(BV)PetscToPointer((bv) ),
	(Vec)PetscToPointer((x) ),
	(Vec)PetscToPointer((y) ));
}
SLEPC_EXTERN void  bvapplymatrixbv_(BV X,BV Y, int *ierr)
{
CHKFORTRANNULLOBJECT(X);
CHKFORTRANNULLOBJECT(Y);
*ierr = BVApplyMatrixBV(
	(BV)PetscToPointer((X) ),
	(BV)PetscToPointer((Y) ));
}
SLEPC_EXTERN void  bvsetsignature_(BV bv,Vec omega, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(omega);
*ierr = BVSetSignature(
	(BV)PetscToPointer((bv) ),
	(Vec)PetscToPointer((omega) ));
}
SLEPC_EXTERN void  bvgetsignature_(BV bv,Vec omega, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(omega);
*ierr = BVGetSignature(
	(BV)PetscToPointer((bv) ),
	(Vec)PetscToPointer((omega) ));
}
SLEPC_EXTERN void  bvsetbuffervec_(BV bv,Vec buffer, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(buffer);
*ierr = BVSetBufferVec(
	(BV)PetscToPointer((bv) ),
	(Vec)PetscToPointer((buffer) ));
}
SLEPC_EXTERN void  bvgetbuffervec_(BV bv,Vec *buffer, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool buffer_null = !*(void**) buffer ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(buffer);
*ierr = BVGetBufferVec(
	(BV)PetscToPointer((bv) ),buffer);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! buffer_null && !*(void**) buffer) * (void **) buffer = (void *)-2;
}
SLEPC_EXTERN void  bvsetrandomcontext_(BV bv,PetscRandom rand, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(rand);
*ierr = BVSetRandomContext(
	(BV)PetscToPointer((bv) ),
	(PetscRandom)PetscToPointer((rand) ));
}
SLEPC_EXTERN void  bvgetrandomcontext_(BV bv,PetscRandom* rand, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool rand_null = !*(void**) rand ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(rand);
*ierr = BVGetRandomContext(
	(BV)PetscToPointer((bv) ),rand);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! rand_null && !*(void**) rand) * (void **) rand = (void *)-2;
}
SLEPC_EXTERN void  bvsetfromoptions_(BV bv, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
*ierr = BVSetFromOptions(
	(BV)PetscToPointer((bv) ));
}
SLEPC_EXTERN void  bvsetorthogonalization_(BV bv,BVOrthogType *type,BVOrthogRefineType *refine,PetscReal *eta,BVOrthogBlockType *block, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
*ierr = BVSetOrthogonalization(
	(BV)PetscToPointer((bv) ),*type,*refine,*eta,*block);
}
SLEPC_EXTERN void  bvgetorthogonalization_(BV bv,BVOrthogType *type,BVOrthogRefineType *refine,PetscReal *eta,BVOrthogBlockType *block, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLREAL(eta);
*ierr = BVGetOrthogonalization(
	(BV)PetscToPointer((bv) ),type,refine,eta,block);
}
SLEPC_EXTERN void  bvsetmatmultmethod_(BV bv,BVMatMultType *method, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
*ierr = BVSetMatMultMethod(
	(BV)PetscToPointer((bv) ),*method);
}
SLEPC_EXTERN void  bvgetmatmultmethod_(BV bv,BVMatMultType *method, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
*ierr = BVGetMatMultMethod(
	(BV)PetscToPointer((bv) ),method);
}
SLEPC_EXTERN void  bvgetcolumn_(BV bv,PetscInt *j,Vec *v, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool v_null = !*(void**) v ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(v);
*ierr = BVGetColumn(
	(BV)PetscToPointer((bv) ),*j,v);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! v_null && !*(void**) v) * (void **) v = (void *)-2;
}
SLEPC_EXTERN void  bvrestorecolumn_(BV bv,PetscInt *j,Vec *v, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool v_null = !*(void**) v ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(v);
*ierr = BVRestoreColumn(
	(BV)PetscToPointer((bv) ),*j,v);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! v_null && !*(void**) v) * (void **) v = (void *)-2;
}
SLEPC_EXTERN void  bvcreatevec_(BV bv,Vec *v, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool v_null = !*(void**) v ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(v);
*ierr = BVCreateVec(
	(BV)PetscToPointer((bv) ),v);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! v_null && !*(void**) v) * (void **) v = (void *)-2;
}
SLEPC_EXTERN void  bvcreatevecempty_(BV bv,Vec *v, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool v_null = !*(void**) v ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(v);
*ierr = BVCreateVecEmpty(
	(BV)PetscToPointer((bv) ),v);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! v_null && !*(void**) v) * (void **) v = (void *)-2;
}
SLEPC_EXTERN void  bvsetvectype_(BV bv,char *vtype, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(bv);
/* insert Fortran-to-C conversion for vtype */
  FIXCHAR(vtype,cl0,_cltmp0);
*ierr = BVSetVecType(
	(BV)PetscToPointer((bv) ),_cltmp0);
  FREECHAR(vtype,_cltmp0);
}
SLEPC_EXTERN void  bvgetvectype_(BV bv,char *vtype, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(bv);
*ierr = BVGetVecType(
	(BV)PetscToPointer((bv) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for vtype */
*ierr = PetscStrncpy(vtype, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, vtype, cl0);
}
SLEPC_EXTERN void  bvcreatemat_(BV bv,Mat *A, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
*ierr = BVCreateMat(
	(BV)PetscToPointer((bv) ),A);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
}
SLEPC_EXTERN void  bvgetmat_(BV bv,Mat *A, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
*ierr = BVGetMat(
	(BV)PetscToPointer((bv) ),A);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
}
SLEPC_EXTERN void  bvrestoremat_(BV bv,Mat *A, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
*ierr = BVRestoreMat(
	(BV)PetscToPointer((bv) ),A);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
}
SLEPC_EXTERN void  bvduplicate_(BV V,BV *W, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
PetscBool W_null = !*(void**) W ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(W);
*ierr = BVDuplicate(
	(BV)PetscToPointer((V) ),W);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! W_null && !*(void**) W) * (void **) W = (void *)-2;
}
SLEPC_EXTERN void  bvduplicateresize_(BV V,PetscInt *m,BV *W, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
PetscBool W_null = !*(void**) W ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(W);
*ierr = BVDuplicateResize(
	(BV)PetscToPointer((V) ),*m,W);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! W_null && !*(void**) W) * (void **) W = (void *)-2;
}
SLEPC_EXTERN void  bvgetcachedbv_(BV bv,BV *cached, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool cached_null = !*(void**) cached ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(cached);
*ierr = BVGetCachedBV(
	(BV)PetscToPointer((bv) ),cached);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! cached_null && !*(void**) cached) * (void **) cached = (void *)-2;
}
SLEPC_EXTERN void  bvcopy_(BV V,BV W, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
CHKFORTRANNULLOBJECT(W);
*ierr = BVCopy(
	(BV)PetscToPointer((V) ),
	(BV)PetscToPointer((W) ));
}
SLEPC_EXTERN void  bvcopyvec_(BV V,PetscInt *j,Vec w, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
CHKFORTRANNULLOBJECT(w);
*ierr = BVCopyVec(
	(BV)PetscToPointer((V) ),*j,
	(Vec)PetscToPointer((w) ));
}
SLEPC_EXTERN void  bvcopycolumn_(BV V,PetscInt *j,PetscInt *i, int *ierr)
{
CHKFORTRANNULLOBJECT(V);
*ierr = BVCopyColumn(
	(BV)PetscToPointer((V) ),*j,*i);
}
SLEPC_EXTERN void  bvgetsplit_(BV bv,BV *L,BV *R, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool L_null = !*(void**) L ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(L);
PetscBool R_null = !*(void**) R ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(R);
*ierr = BVGetSplit(
	(BV)PetscToPointer((bv) ),L,R);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! L_null && !*(void**) L) * (void **) L = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! R_null && !*(void**) R) * (void **) R = (void *)-2;
}
SLEPC_EXTERN void  bvrestoresplit_(BV bv,BV *L,BV *R, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
PetscBool L_null = !*(void**) L ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(L);
PetscBool R_null = !*(void**) R ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(R);
*ierr = BVRestoreSplit(
	(BV)PetscToPointer((bv) ),L,R);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! L_null && !*(void**) L) * (void **) L = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! R_null && !*(void**) R) * (void **) R = (void *)-2;
}
SLEPC_EXTERN void  bvgetsplitrows_(BV bv,IS isup,IS islo,BV *U,BV *L, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(isup);
CHKFORTRANNULLOBJECT(islo);
PetscBool U_null = !*(void**) U ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(U);
PetscBool L_null = !*(void**) L ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(L);
*ierr = BVGetSplitRows(
	(BV)PetscToPointer((bv) ),
	(IS)PetscToPointer((isup) ),
	(IS)PetscToPointer((islo) ),U,L);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! U_null && !*(void**) U) * (void **) U = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! L_null && !*(void**) L) * (void **) L = (void *)-2;
}
SLEPC_EXTERN void  bvrestoresplitrows_(BV bv,IS isup,IS islo,BV *U,BV *L, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLOBJECT(isup);
CHKFORTRANNULLOBJECT(islo);
PetscBool U_null = !*(void**) U ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(U);
PetscBool L_null = !*(void**) L ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(L);
*ierr = BVRestoreSplitRows(
	(BV)PetscToPointer((bv) ),
	(IS)PetscToPointer((isup) ),
	(IS)PetscToPointer((islo) ),U,L);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! U_null && !*(void**) U) * (void **) U = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! L_null && !*(void**) L) * (void **) L = (void *)-2;
}
SLEPC_EXTERN void  bvsetdefinitetolerance_(BV bv,PetscReal *deftol, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
*ierr = BVSetDefiniteTolerance(
	(BV)PetscToPointer((bv) ),*deftol);
}
SLEPC_EXTERN void  bvgetdefinitetolerance_(BV bv,PetscReal *deftol, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLREAL(deftol);
*ierr = BVGetDefiniteTolerance(
	(BV)PetscToPointer((bv) ),deftol);
}
SLEPC_EXTERN void  bvsetleadingdimension_(BV bv,PetscInt *ld, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
*ierr = BVSetLeadingDimension(
	(BV)PetscToPointer((bv) ),*ld);
}
SLEPC_EXTERN void  bvgetleadingdimension_(BV bv,PetscInt *ld, int *ierr)
{
CHKFORTRANNULLOBJECT(bv);
CHKFORTRANNULLINTEGER(ld);
*ierr = BVGetLeadingDimension(
	(BV)PetscToPointer((bv) ),ld);
}
#if defined(__cplusplus)
}
#endif
